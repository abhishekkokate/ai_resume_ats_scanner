import logging

from google.adk.agents import SequentialAgent, ParallelAgent

from .sub_agents import (
    intake_agent,
    resume_agent,
    jd_agent,
    compare_agent,
)

logging.basicConfig(
    filename="logger.log",
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
)

logger = logging.getLogger(__name__)

print("✅ Logging configured")

parallel_agent = ParallelAgent(
    name="ParallelResumeJDParsingAgent",
    description="Parses resume and JD in parallel.",
    sub_agents=[resume_agent, jd_agent],
)

logger.info("✅ Parallel agent configured")

root_agent = SequentialAgent(
    name="ResumeATSRootAgent",
    description="Collects resume and JD. Passes them to special parallel agents for resume and JD parsing. Then compares them to produce ATS-style scoring with strengths, gaps, and improvement suggestions.",
    sub_agents=[intake_agent, parallel_agent, compare_agent],
)

logger.info("✅ Root agent configured")
