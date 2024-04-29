import React, { useState, useEffect } from 'react';
import SearchForm from './components/SearchForm';
import PublicationList from './components/PublicationList';
import Pagination from './components/Pagination';
import PublicationDetails from './components/PublicationDetails';
import { fetchPublications, fetchPublicationDetails } from './api/api';

const App = () => {
  const [query, setQuery] = useState('');
  const [publications, setPublications] = useState([]);
  const [selectedPublication, setSelectedPublication] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    // Fetch publications when the component mounts
    fetchResults(query, currentPage);
  }, [query, currentPage]);

  const fetchResults = async (query, page) => {
    try {
      const response = await fetch(`http://localhost:8000/search_publications`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query }) // Send query parameter in the request body
      });
      const data = await response.json();
      setPublications(data.publication_ids);
    } catch (error) {
      console.error('Error fetching results:', error);
    }
  };

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  const handleViewDetails = (publication) => {
    setSelectedPublication(publication);
  };

  const handleBackToList = () => {
    setSelectedPublication(null);
  };

  return (
    <div>
      <h1>Publication Search</h1>
      {!selectedPublication ? (
        <>
          <SearchForm onSubmit={(query) => setQuery(query)} />
          <PublicationList publications={publications} onViewDetails={handleViewDetails} />
          <Pagination currentPage={currentPage} totalPages={totalPages} onPageChange={handlePageChange} />
        </>
      ) : (
        <>
          <PublicationDetails publication={selectedPublication} />
          <button onClick={handleBackToList}>Back to List</button>
        </>
      )}
    </div>
  );
};

export default App;
