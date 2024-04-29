import React from 'react';
import PublicationItem from './PublicationItem';

const PublicationList = ({ publications }) => {
  return (
    <ul>
      {publications.map((publication) => (
        <PublicationItem key={publication.PMID} publication={publication} />
      ))}
    </ul>
  );
};

export default PublicationList;