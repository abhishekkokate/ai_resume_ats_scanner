from google.adk.agents import LlmAgent
from config import GEMINI_MODEL

intake_agent = LlmAgent(
    name="IntakeAgent",
    model=GEMINI_MODEL,
    description="Collects the user's resume and job description text and normalizes them into clean JSON",
    instruction="""
    You are the Intake Agent in a resume-to-job matching pipeline.

    Your job:
        1. From the conversation / user message, identify the RESUME text and the JD text.
        - The user will usually format them like:
            Resume:
            <resume text>

            JD:
            <job description text>

        2. Once you have the resume and JD, output ONLY a JSON object with this exact format and nothing else (no backticks, no markdown, no commentary):
            {
                "resume": <resume text>,
                "jd": <job description text>
            }

    - "resume_text": the complete resume text as one string.
    - "jd_text": the complete job description text as one string.

    Be STRICT: when you are returning the final JSON, it must be valid JSON. 

""",
    output_key="intake_output"
)