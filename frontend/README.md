# AI Resume Reviewer - Frontend

A modern React application for AI-powered resume analysis and feedback.

## Features

- 📄 **File Upload**: Drag & drop or click to upload PDF/DOCX resumes
- 💼 **Job Description**: Optional job description input for personalized feedback
- 🎯 **Match Score**: Keyword matching and job compatibility scoring
- 📊 **Readability Analysis**: Multiple readability metrics and grade levels
- ✏️ **Grammar Check**: Basic grammar and style validation
- 🤖 **AI Feedback**: GPT-powered comprehensive feedback and suggestions
- 💡 **Rewrite Suggestions**: Specific improvement recommendations

## Getting Started

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5173`

## Backend Integration

Make sure your FastAPI backend is running before using the frontend.

### API Configuration

The frontend is configured to connect to the backend API. You can customize the API URL by setting the `VITE_API_BASE_URL` environment variable:

```bash
# Create a .env file in the frontend directory
VITE_API_BASE_URL=http://127.0.0.1:8000
```

**Default configuration:**
- Development: `http://127.0.0.1:8000`
- Production: Set `VITE_API_BASE_URL` to your production API URL

The configuration is managed in `src/config.js` and supports environment variable overrides.

## Build for Production

```bash
npm run build
```

## Technologies Used

- React 18
- Vite
- Modern CSS with gradients and animations
- Responsive design
- Drag & drop file upload
