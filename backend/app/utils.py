import pdfplumber
from docx import Document
import re
import textstat
from typing import List, Tuple
import openai
import os
from collections import Counter

def extract_text_from_pdf(file_path: str) -> str:
    try:
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() or '' for page in pdf.pages)
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF text: {e}"

def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        return f"Error extracting DOCX text: {e}"

def extract_keywords(text: str) -> List[str]:
    """Extract important keywords from text (basic implementation)"""
    # Remove common words and extract meaningful terms
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
    
    # Extract words (basic approach)
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    
    # Return unique keywords with frequency
    keyword_freq = Counter(keywords)
    return [word for word, freq in keyword_freq.most_common(20)]

def calculate_match_score(resume_keywords: List[str], job_keywords: List[str]) -> float:
    """Calculate match score between resume and job description keywords"""
    if not job_keywords:
        return 0.0
    
    resume_set = set(resume_keywords)
    job_set = set(job_keywords)
    
    # Calculate intersection
    common_keywords = resume_set.intersection(job_set)
    
    # Calculate match score as percentage
    match_score = len(common_keywords) / len(job_set) * 100
    return round(match_score, 2)

def analyze_readability(text: str) -> dict:
    """Analyze text readability using textstat"""
    try:
        return {
            "flesch_reading_ease": textstat.flesch_reading_ease(text),
            "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
            "gunning_fog": textstat.gunning_fog(text),
            "smog_index": textstat.smog_index(text),
            "automated_readability_index": textstat.automated_readability_index(text),
            "coleman_liau_index": textstat.coleman_liau_index(text),
            "linsear_write_formula": textstat.linsear_write_formula(text),
            "dale_chall_readability_score": textstat.dale_chall_readability_score(text),
            "difficult_words": textstat.difficult_words(text),
            "syllable_count": textstat.syllable_count(text),
            "lexicon_count": textstat.lexicon_count(text),
            "sentence_count": textstat.sentence_count(text)
        }
    except Exception as e:
        return {"error": f"Readability analysis failed: {e}"}

def basic_grammar_check(text: str) -> List[str]:
    """Basic grammar checking (placeholder for more sophisticated analysis)"""
    issues = []
    
    # Check for common issues
    sentences = text.split('.')
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Check for sentence starting with lowercase
        if sentence and sentence[0].islower():
            issues.append(f"Sentence {i+1}: Should start with capital letter")
        
        # Check for double spaces
        if '  ' in sentence:
            issues.append(f"Sentence {i+1}: Contains double spaces")
    
    return issues

def get_missing_keywords(resume_keywords: List[str], job_keywords: List[str]) -> List[str]:
    """Find keywords from job description that are missing in resume"""
    resume_set = set(resume_keywords)
    job_set = set(job_keywords)
    
    missing = job_set - resume_set
    return list(missing)[:10]  # Return top 10 missing keywords 

def generate_gpt_feedback(resume_text: str, job_description: str = None, analysis_results: dict = None) -> str:
    """Generate AI-powered feedback using OpenAI GPT"""
    try:
        # Set up OpenAI client (you'll need to set OPENAI_API_KEY environment variable)
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Prepare the prompt
        prompt = f"""
        Analyze this resume and provide constructive feedback:

        RESUME TEXT:
        {resume_text}

        JOB DESCRIPTION (if provided):
        {job_description if job_description else "No job description provided"}

        ANALYSIS RESULTS:
        - Match Score: {analysis_results.get('match_score', 'N/A')}%
        - Missing Keywords: {', '.join(analysis_results.get('missing_keywords', []))}
        - Grammar Issues: {len(analysis_results.get('grammar_issues', []))} found
        - Readability Score: {analysis_results.get('readability', {}).get('flesch_reading_ease', 'N/A')}

        Please provide:
        1. Overall assessment (strengths and weaknesses)
        2. Specific suggestions for improvement
        3. Content recommendations
        4. Formatting suggestions
        5. Action items to enhance the resume

        Keep the feedback constructive and actionable.
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer and career coach. Provide constructive, actionable feedback."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Unable to generate AI feedback: {e}. Please check your OpenAI API key configuration."

def get_suggested_rewrites(resume_text: str, job_description: str = None) -> List[str]:
    """Get specific rewrite suggestions for resume sections"""
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        prompt = f"""
        Review this resume and provide 3-5 specific rewrite suggestions for bullet points or sentences:

        RESUME TEXT:
        {resume_text}

        JOB DESCRIPTION:
        {job_description if job_description else "No specific job description provided"}

        Provide specific rewrites that:
        1. Use action verbs
        2. Include quantifiable results
        3. Are more impactful
        4. Better match the job requirements

        Format each suggestion as: "Original: [text] → Improved: [text]"
        """
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume writer. Provide specific, actionable rewrite suggestions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        # Split the response into individual suggestions
        suggestions = response.choices[0].message.content.split('\n')
        return [s.strip() for s in suggestions if s.strip() and '→' in s]
        
    except Exception as e:
        return [f"Unable to generate rewrite suggestions: {e}"] 