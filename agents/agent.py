from google.adk.agents import SequentialAgent, ParallelAgent

from .sub_agents import (
    intake_agent,
    resume_agent,
    jd_agent,
    compare_agent,
)

parallel_agent = ParallelAgent(
    name="ParallelResumeJDParsingAgent",
    description="Parses resume and JD in parallel.",
    sub_agents=[resume_agent, jd_agent],
)

root_agent = SequentialAgent(
    name="ResumeATSRootAgent",
    description="Collects resume and JD. Passes them to special parallel agents for resume and JD parsing. Then compares them to produce ATS-style scoring with strengths, gaps, and improvement suggestions.",
    sub_agents=[intake_agent, parallel_agent, compare_agent],
)
