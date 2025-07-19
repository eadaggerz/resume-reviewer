from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import os
from .utils import (
    extract_text_from_pdf, 
    extract_text_from_docx,
    extract_keywords,
    calculate_match_score,
    analyze_readability,
    basic_grammar_check,
    get_missing_keywords,
    generate_gpt_feedback,
    get_suggested_rewrites
)

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-resume/")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: Optional[str] = Form(None)
):
    contents = await resume.read()
    filename = resume.filename
    temp_path = f"temp_{filename}"
    with open(temp_path, "wb") as f:
        f.write(contents)
    
    # Extract text based on file extension
    ext = filename.lower().split(".")[-1]
    if ext == "pdf":
        resume_text = extract_text_from_pdf(temp_path)
    elif ext == "docx":
        resume_text = extract_text_from_docx(temp_path)
    else:
        resume_text = "Unsupported file type. Please upload a PDF or DOCX."
    
    # Clean up temp file
    os.remove(temp_path)
    
    # Analyze resume
    resume_keywords = extract_keywords(resume_text)
    readability_analysis = analyze_readability(resume_text)
    grammar_issues = basic_grammar_check(resume_text)
    
    # Job description analysis (if provided)
    job_keywords = []
    match_score = 0.0
    missing_keywords = []
    
    if job_description:
        job_keywords = extract_keywords(job_description)
        match_score = calculate_match_score(resume_keywords, job_keywords)
        missing_keywords = get_missing_keywords(resume_keywords, job_keywords)
    
    # Prepare analysis results for GPT
    analysis_results = {
        "match_score": match_score,
        "missing_keywords": missing_keywords,
        "grammar_issues": grammar_issues,
        "readability": readability_analysis
    }
    
    # Generate AI feedback
    gpt_feedback = generate_gpt_feedback(resume_text, job_description, analysis_results)
    suggested_rewrites = get_suggested_rewrites(resume_text, job_description)
    
    return JSONResponse({
        "resume_filename": filename,
        "resume_text": resume_text,
        "job_description": job_description,
        "analysis": {
            "resume_keywords": resume_keywords,
            "job_keywords": job_keywords,
            "match_score": match_score,
            "missing_keywords": missing_keywords,
            "readability": readability_analysis,
            "grammar_issues": grammar_issues
        },
        "ai_feedback": {
            "general_feedback": gpt_feedback,
            "suggested_rewrites": suggested_rewrites
        }
    }) 