# Heimdrw Core

A modern web application built with React and FastAPI.

## Project Structure

```
heimdrw-core/
├── frontend/           # React frontend application
├── backend/           # FastAPI backend application
└── README.md         # Project documentation
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Development

- Backend runs on http://localhost:8000
- Frontend runs on http://localhost:3000
- API documentation available at http://localhost:8000/docs