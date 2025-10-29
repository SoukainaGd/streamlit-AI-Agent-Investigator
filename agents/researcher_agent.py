# agents/researcher_agent.py
from crewai import Agent, LLM
from crewai.tools import tool
from tools.web_search_tool import search_web   # use the tool you already built
from dotenv import load_dotenv
import os

load_dotenv()

from crewai import LLM
import time

def create_llm_with_retry(model="groq/llama-3.1-8b-instant", retries=3, delay=5):
    for attempt in range(retries):
        try:
            return LLM(model=model, temperature=0.2)
        except Exception as e:
            if "rate_limit_exceeded" in str(e).lower():
                wait = delay * (2 ** attempt)
                print(f"⚠️ Rate limit hit, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("LLM initialization failed after retries")

llm = create_llm_with_retry()


@tool("Research Tool")
def research_tool(query: str, top: int = 6):
    """
    Searches the web using SerpAPI and returns URLs, titles, and snippets.
    """
    return search_web.run(query, num_results=top)


researcher_agent = Agent(
    role="Open-source researcher",
    goal="Collect and summarize verifiable public information with citations.",
    backstory="Expert OSINT analyst focused on transparency and sourcing.",
    llm=llm,
    tools=[research_tool],
    verbose=True
)
