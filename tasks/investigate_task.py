# tasks/investigate_task.py
from crewai import Task
from agents.researcher_agent import researcher_agent
from agents.verifier_agent import verifier_agent

investigate_company = Task(
    description="Investigate Company X for public evidence of supplying goods/services linked to military operations",
    expected_output="Structured JSON claims with provenance and confidence levels",
    agent=researcher_agent
)
