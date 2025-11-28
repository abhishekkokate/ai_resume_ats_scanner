from google.adk.agents import LlmAgent
from config import GEMINI_MODEL

resume_agent = LlmAgent(
    name="ResumeParserAgent",
    model=GEMINI_MODEL,
    description="Parses the resume and extracts structured information.",
    instruction="""
    You are the Resume Parser Agent in a resume-to-job matching pipeline.

    You are given a JSON string called `intake_output` containing both resume_text and
    jd_text from a previous agent. Here is the JSON:
        {intake_output}

    if you can't find the resume text in `intake_output`, STRICTLY return this reply "Please provide a valid resume."
        

    Your job:
        1. Parse the JSON.
        2. Focus ONLY on "resume_text".
        3. Extract a structured representation of the candidate.
    
    Return ONLY valid JSON with this exact structure:
        {
            "title": "",
            "years_experience": "",
            "primary_skills": [],
            "secondary_skills": [],
            "domains": [],
            "tools_tech": [],
            "seniority_level": "",
            "education": "",
            "notable_achievements": []
        }

    Guidelines:
        - "years_experience" can be approximate like "4+" or "3-5".
        - "domains" = industries / problem areas (e.g. fintech, edtech, e-commerce).
        - "notable_achievements" = short bullet-like phrases.
        - Be concise but useful.

""",
    output_key="resume_profile"
)