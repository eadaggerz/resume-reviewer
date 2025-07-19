# AI-Powered Resume Reviewer Backend

This is the backend for the AI-Powered Resume Reviewer MVP, built with FastAPI.

## Features
- Upload resume (PDF or DOCX)
- Paste job description (optional)
- Extract text from resume
- Analyze readability, grammar, structure
- Match resume keywords with job description
- Generate feedback using GPT

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ``` 