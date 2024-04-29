import React from 'react';

const PublicationDetails = ({ publication }) => {
  // Display detailed information of the selected publication
  return (
    <div>
      <h2>{publication.Title}</h2>
      <p>{publication.Abstract}</p>
      <p>{publication.AuthorList}</p>
      <p>{publication.Journal}</p>
      <p>{publication.PublicationYear}</p>
      <p>{publication.MeSHTerms}</p>
      <a href={publication.Link} target="_blank" rel="noopener noreferrer">Original Webpage</a>
    </div>
  );
};

export default PublicationDetails;