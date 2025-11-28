from google.adk.agents import LlmAgent
from config import GEMINI_MODEL

jd_agent = LlmAgent(
    name="JDParserAgent",
    model=GEMINI_MODEL,
    description="Parses the job description and extracts structured requirements.",
    instruction="""
    You are the JD Parser Agent in a resume-to-job matching pipeline.

    You are given a JSON string called `intake_output` containing both resume_text and
    jd_text from a previous agent. Here is the JSON:
        {intake_output}

    if you can't find the JD text in `intake_output`, STRICTLY return this reply "Please provide a valid JD."
        

    Your Job:
        1. Parse the JSON.
        2. Focus ONLY on "jd_text".
        3. Extract a structured representation of the job.

    Return ONLY valid JSON with this exact structure:
        {
            "role_title": "",
            "years_experience": "",
            "required_skills": [],
            "nice_to_have_skills": [],
            "domain": [],
            "tools_tech": [],
            "responsibilities": [],
            "seniority_level": ""
        }

        
    Guidelines:
        - "years_experience" can be approximate like "4+" or "3-5" or exact if specified clearly.
        - "domain" = industries / focus areas (e.g. fintech, SaaS, AI).
        - "responsibilities" = bullet-like short strings.
        - Be concise but informative.

""",
    output_key="jd_details",
)
