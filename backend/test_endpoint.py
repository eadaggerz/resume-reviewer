import requests
import json

def test_resume_analysis():
    """Test the resume analysis endpoint"""
    
    # Sample resume text (you can replace this with actual file upload)
    sample_resume_text = """
    JOHN DOE
    Software Engineer
    
    EXPERIENCE
    Senior Developer at Tech Corp (2020-2023)
    - Developed web applications using React and Python
    - Led team of 5 developers
    - Improved system performance by 25%
    
    SKILLS
    Python, JavaScript, React, FastAPI, SQL
    """
    
    # Sample job description
    sample_job_description = """
    We are looking for a Software Engineer with experience in:
    - Python development
    - React frontend development
    - API development with FastAPI
    - Database management with SQL
    - Team leadership experience
    """
    
    # Test data
    test_data = {
        'resume': ('test_resume.txt', sample_resume_text, 'text/plain'),
        'job_description': sample_job_description
    }
    
    try:
        # Make request to the endpoint
        response = requests.post(
            'http://127.0.0.1:8000/analyze-resume/',
            files={'resume': test_data['resume']},
            data={'job_description': test_data['job_description']}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Analysis successful!")
            print(f"Match Score: {result['analysis']['match_score']}%")
            print(f"Missing Keywords: {result['analysis']['missing_keywords']}")
            print(f"Grammar Issues: {len(result['analysis']['grammar_issues'])}")
            print(f"AI Feedback: {result['ai_feedback']['general_feedback']}...")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Make sure the server is running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_resume_analysis() 