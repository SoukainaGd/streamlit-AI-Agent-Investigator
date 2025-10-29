# agents/verifier_agent.py
from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()

llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.0)

verifier_agent = Agent(
    role="Cross-check verifier",
    goal=("Cross-check each claim against at least two independent primary sources and rate confidence."),
    backstory=("You are conservative and require corroboration. You return confidence [0.0-1.0] and cite sources."),
    llm=llm,
    tools=[],  # this agent can use network tools if needed
    verbose=True
)
