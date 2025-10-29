# agents/verifier_agent.py
from crewai import Agent, LLM
from dotenv import load_dotenv
import time
import os

load_dotenv()

def create_llm_with_retry(model="gpt-4o-mini", retries=3, delay=5):
    for attempt in range(retries):
        try:
            return LLM(model=model, temperature=0.0)
        except Exception as e:
            if "rate_limit" in str(e).lower():
                wait = delay * (2 ** attempt)
                print(f"⚠️ Rate limit hit, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("LLM initialization failed after retries")

llm = create_llm_with_retry()

verifier_agent = Agent(
    role="Cross-check verifier",
    goal=(
        "Cross-check each claim against at least two independent primary sources and rate confidence."
    ),
    backstory=(
        "You are conservative and require corroboration. "
        "You return confidence [0.0–1.0] and cite sources."
    ),
    llm=llm,
    tools=[],  # add verification tools later if needed
    verbose=True
)
