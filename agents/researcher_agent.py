# agents/researcher_agent.py
from crewai import Agent, LLM
from crewai.tools import tool
from tools.web_search_tool import search_web
from dotenv import load_dotenv
import os
import time

load_dotenv()

# --- Create LLM with retry for OpenAI ---
def create_llm_with_retry(model="gpt-4o-mini", retries=3, delay=5):
    """
    Initializes the OpenAI LLM with retry logic if rate limits occur.
    """
    for attempt in range(retries):
        try:
            return LLM(
                model=model,
                temperature=0.2,
                api_key=os.getenv("OPENAI_API_KEY")  # load from .env or Streamlit secrets
            )
        except Exception as e:
            if "rate_limit" in str(e).lower():
                wait = delay * (2 ** attempt)
                print(f"⚠️ OpenAI rate limit hit, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("❌ OpenAI LLM initialization failed after retries")

# Use GPT model from OpenAI
llm = create_llm_with_retry()

# --- Define your search tool ---
@tool("Research Tool")
def research_tool(query: str, top: int = 6):
    """
    Searches the web using SerpAPI and returns URLs, titles, and snippets.
    """
    return search_web.run(query, num_results=top)

# --- Define your researcher agent ---
researcher_agent = Agent(
    role="Open-source researcher",
    goal="Collect and summarize verifiable public information with citations.",
    backstory="Expert OSINT analyst specialized in investigating corporate and political relationships.",
    llm=llm,
    tools=[research_tool],
    verbose=True
)
