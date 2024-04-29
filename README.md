# PubMed Publication Search

This project is a web application that allows users to search for publications on PubMed and view detailed information about them.

## Features

- Users can input a query and submit it to search for publications.
- Basic information about the search results, including ID, title, and year, is displayed in a list.
- Pagination support allows users to navigate through multiple pages of search results.
- Users can view detailed information about a selected publication.
- Each publication item includes a link to the original webpage for further reference.

## Technologies Used

- Frontend: React.js
- Backend: FastAPI (Python)
- PubMed API: E-utilities provided by NCBI

## Setup Instructions

1. Clone the repository:\
git clone <repository-url>

2. Navigate to the project directory:\
cd pubmed-publication-search

3. Install dependencies:\
cd frontend\
npm install\
cd ../backend\
pip install -r requirements.txt

4. Start the backend server:/
cd backend/
uvicorn main:app --reload

5. Start the frontend development server:/
cd frontend/
npm start

6. Open your browser and go to `http://localhost:3000` to access the application.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.


