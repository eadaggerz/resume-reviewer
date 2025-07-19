from pydantic import BaseModel
from typing import List, Optional

class ResumeAnalysisResponse(BaseModel):
    resume_text: str
    job_description: Optional[str]
    match_score: Optional[float]
    missing_keywords: Optional[List[str]]
    feedback: Optional[str]
    suggested_rewrites: Optional[List[str]] 