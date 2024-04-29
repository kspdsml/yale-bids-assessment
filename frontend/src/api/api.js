const BASE_URL = 'http://localhost:8000'; // Your FastAPI backend base URL

const fetchPublications = async (query) => {
  const response = await fetch(`${BASE_URL}/search_publications?query=${query}`);
  if (!response.ok) {
    throw new Error('Failed to fetch publications');
  }
  const data = await response.json();
  return data.publication_ids;
};

const fetchPublicationDetails = async (pubIds) => {
  const response = await fetch(`${BASE_URL}/publication_details?pub_ids=${pubIds}`);
  if (!response.ok) {
    throw new Error('Failed to fetch publication details');
  }
  const data = await response.json();
  return data.publications;
};

export { fetchPublications, fetchPublicationDetails };