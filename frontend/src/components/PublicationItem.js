import React from 'react';

const PublicationItem = ({ publication }) => {
  const { PMID, Title, PublicationYear } = publication;

  return (
    <li>
      <div>{PMID}</div>
      <div>{Title}</div>
      <div>{PublicationYear}</div>
    </li>
  );
};

export default PublicationItem;