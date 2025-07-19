# 🤖 AI Resume Reviewer

A comprehensive AI-powered resume analysis tool that provides detailed feedback, keyword matching, readability analysis, and personalized suggestions to help job seekers improve their resumes.

## ✨ Features

### 📊 Analysis Capabilities
- **Text Extraction**: Supports PDF and DOCX resume formats
- **Keyword Matching**: Compares resume keywords with job descriptions
- **Readability Analysis**: Multiple metrics including Flesch Reading Ease, Grade Level
- **Grammar Checking**: Basic grammar and style validation
- **AI-Powered Feedback**: GPT-generated comprehensive feedback and suggestions

### 🎯 Job Matching
- **Match Score**: Percentage-based compatibility with job descriptions
- **Missing Keywords**: Identifies important keywords not found in resume
- **Keyword Extraction**: Automatically extracts relevant terms from both resume and job posting

### 💡 Smart Suggestions
- **Rewrite Suggestions**: Specific improvements for bullet points and sentences
- **Action Items**: Clear next steps for resume enhancement
- **Formatting Tips**: Professional formatting recommendations

## 🏗️ Architecture

```
resume-reviewer/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # API endpoints
│   │   ├── utils.py        # Analysis functions
│   │   └── models.py       # Data models
│   ├── requirements.txt    # Python dependencies
│   └── README.md          # Backend documentation
├── frontend/               # React + Vite frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.jsx        # Main application
│   │   └── App.css        # Styling
│   ├── package.json       # Node dependencies
│   └── README.md          # Frontend documentation
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API key:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

5. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

The backend will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173`

## 📖 Usage

### 1. Upload Resume
- Drag and drop or click to upload your resume (PDF or DOCX)
- The system will automatically extract and analyze the text

### 2. Add Job Description (Optional)
- Paste a job description for personalized feedback
- This enables keyword matching and job-specific suggestions

### 3. Get Analysis
- Click "Analyze Resume" to process your document
- View comprehensive results including:
  - Job match score
  - Missing keywords
  - Readability metrics
  - Grammar issues
  - AI-generated feedback

### 4. Review Suggestions
- Read through the detailed feedback
- Implement suggested improvements
- Use the rewrite suggestions for specific enhancements

## 🛠️ API Endpoints

### POST `/analyze-resume/`
Analyzes a resume and provides comprehensive feedback.

**Request:**
- `resume`: File upload (PDF/DOCX)
- `job_description`: String (optional)

**Response:**
```json
{
  "resume_filename": "resume.pdf",
  "resume_text": "Extracted text content...",
  "job_description": "Job description text...",
  "analysis": {
    "resume_keywords": ["python", "react", "fastapi"],
    "job_keywords": ["python", "javascript", "sql"],
    "match_score": 75.5,
    "missing_keywords": ["javascript", "sql"],
    "readability": {
      "flesch_reading_ease": 65.2,
      "flesch_kincaid_grade": 8.1
    },
    "grammar_issues": ["Sentence 1: Should start with capital letter"]
  },
  "ai_feedback": {
    "general_feedback": "Markdown formatted feedback...",
    "suggested_rewrites": ["Original: text → Improved: text"]
  }
}
```

## 🎨 Design System

The application uses a clean, modern color scheme:

| Name            | Hex       | Usage                    |
| --------------- | --------- | ------------------------ |
| Light Gray      | `#F9FAFB` | Main background          |
| Cool Gray       | `#F8FAFC` | Section backgrounds      |
| Soft White      | `#FFFFFF` | Content areas            |
| Light Blue Tint | `#EFF6FF` | Accent areas             |

## 🔧 Technologies Used

### Backend
- **FastAPI**: Modern Python web framework
- **pdfplumber**: PDF text extraction
- **python-docx**: DOCX file processing
- **textstat**: Readability analysis
- **OpenAI GPT**: AI-powered feedback generation

### Frontend
- **React 18**: UI framework
- **Vite**: Build tool and dev server
- **React Markdown**: Markdown rendering
- **Modern CSS**: Responsive design with gradients

## 📝 Development

### Backend Development
```bash
cd backend
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn app.main:app --reload

# Run tests
python test_endpoint.py
```

### Frontend Development
```bash
cd frontend
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for GPT integration
- The open-source community for the excellent libraries used

---