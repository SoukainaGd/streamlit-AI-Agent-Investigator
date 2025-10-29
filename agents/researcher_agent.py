from crewai import Agent, LLM
from crewai.tools import tool
from tools.web_search_tool import search_web
from dotenv import load_dotenv
import os, time

# Load .env locally (Streamlit Cloud ignores this if secrets are set)
load_dotenv()

# ✅ Force environment variables from Streamlit secrets if present
if "GROQ_API_KEY" in os.environ:
    os.environ["GROQ_API_KEY"] = os.environ["GROQ_API_KEY"]
if "SERPAPI_API_KEY" in os.environ:
    os.environ["SERPAPI_API_KEY"] = os.environ["SERPAPI_API_KEY"]

def create_llm_with_retry(model="groq/llama-3.1-8b-instant", retries=3, delay=5):
    for attempt in range(retries):
        try:
            # Make sure API key is available before initializing
            if not os.getenv("GROQ_API_KEY"):
                raise ValueError("❌ GROQ_API_KEY is missing.")
            return LLM(model=model, temperature=0.2)
        except Exception as e:
            if "rate_limit_exceeded" in str(e).lower():
                wait = delay * (2 ** attempt)
                print(f"⚠️ Rate limit hit, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("LLM initialization failed after retries")
