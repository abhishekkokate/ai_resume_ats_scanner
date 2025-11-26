from google.adk.agents import SequentialAgent

from .intake_agent import (
    intake_agent,
)

root_agent = SequentialAgent(
    name="ResumeATSRootAgent",
    description="Collects resume and JD",
    sub_agents=[intake_agent]
)