from fastapi import FastAPI, HTTPException
import requests
import xml.etree.ElementTree as ET
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Function to parse PubMed XML response and extract fields
def parse_pubmed_response(xml_response, fields):
    # Parse the XML response
    root = ET.fromstring(xml_response)

    # Initialize lists to store extracted fields
    publications = []

    # Iterate over each <PubmedArticle> element
    for article in root.findall('.//PubmedArticle'):
        # Initialize dictionary to store extracted fields for this publication
        publication_info = {}

        # Extract fields based on the specified fields parameter
        for field in fields.split(','):
            # Extract field based on the field name
            if field == 'PMID':
                pmid_element = article.find('.//PMID')
                if pmid_element is not None:
                    publication_info['PMID'] = pmid_element.text
            elif field == 'Title':
                title_element = article.find('.//ArticleTitle')
                if title_element is not None:
                    publication_info['Title'] = title_element.text
            elif field == 'Abstract':
                abstract_element = article.find('.//AbstractText')
                if abstract_element is not None:
                    publication_info['Abstract'] = abstract_element.text
            elif field == 'AuthorList':
                authors = article.findall('.//Author')
                author_list = []
                for author in authors:
                    last_name = author.findtext('.//LastName', default='')
                    initials = author.findtext('.//Initials', default='')
                    author_list.append(f"{last_name} {initials}")
                publication_info['AuthorList'] = author_list
            elif field == 'Journal':
                journal_title_element = article.find('.//Journal/Title')
                if journal_title_element is not None:
                    publication_info['Journal'] = journal_title_element.text
            elif field == 'PublicationYear':
                pub_year_element = article.find('.//JournalIssue/PubDate/Year')
                if pub_year_element is not None:
                    publication_info['PublicationYear'] = pub_year_element.text
            elif field == 'MeSHTerms':
                mesh_headings = article.findall('.//MeshHeading/DescriptorName')
                mesh_terms = [mesh_heading.text for mesh_heading in mesh_headings]
                publication_info['MeSHTerms'] = mesh_terms

        # Append the publication information to the list
        publications.append(publication_info)

    return publications

# Endpoint to retrieve publication IDs based on a query
@app.post("/search_publications")
def search_publications(query: str, retstart: int = 0, retmax: int = 10):
    # Construct the PubMed IDs endpoint URL
    pubmed_ids_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retstart={retstart}&retmax={retmax}&term={query}&retmode=json"

    # Make request to PubMed IDs endpoint
    response = requests.get(pubmed_ids_url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch publication IDs")

    # Extract publication IDs from the response
    pub_ids = response.json().get("esearchresult", {}).get("idlist", [])
    return {"publication_ids": pub_ids}

# Endpoint to fetch detailed information for a list of publication IDs
@app.get("/publication_details")
def publication_details(pub_ids: str, fields: str = "PMID,Title,Abstract,AuthorList,Journal,PublicationYear,MeSHTerms"):
    # Construct the PubMed details endpoint URL
    pubmed_details_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pub_ids}&retmode=xml"

    # Make request to PubMed details endpoint
    response = requests.get(pubmed_details_url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch publication details")

    # Parse XML response and extract necessary fields
    publications = parse_pubmed_response(response.content, fields)

    return {"publications": publications}