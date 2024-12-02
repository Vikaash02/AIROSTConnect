# AI-Based Program Recommendation System

## Project Overview
This is a Python-based web application for recommending programs based on user interests and interactions.

## Prerequisites
- Python 3.9+
- PostgreSQL
- Google OAuth Developer Account

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://your-repo-url.git
cd ai-recommendation-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Create a PostgreSQL database
2. Update `DATABASE_URL` in `backend/database.py`
```bash
createdb recommendation_db
```

### 5. Google OAuth Setup
1. Go to Google Cloud Console
2. Create a new project
3. Enable OAuth 2.0
4. Create credentials (OAuth client ID)
5. Update `GOOGLE_CLIENT_ID` in `backend/auth.py`

### 6. Environment Variables
Create a `.env` file in the project root:
```
DATABASE_URL=postgresql://user:password@localhost/recommendation_db
SECRET_KEY=your-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
```

### 7. Run Migrations
```bash
alembic revision --autogenerate -m "Initial
