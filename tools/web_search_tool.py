# tools/web_search_tool.py
from crewai.tools import tool
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

# ✅ Load your .env file (must be in the same folder as crew.py)
load_dotenv()

# ✅ Get the key from the environment (DO NOT hard-code it here)
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

@tool("Web Search Tool")
def search_web(query: str, num_results: int = 10):
    """
    Searches the web using SerpAPI and returns a list of results with title, URL, and snippet.
    """
    if not SERPAPI_API_KEY:
        raise ValueError("❌ Missing SERPAPI_API_KEY in .env file")

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    items = results.get("organic_results", [])

    output = []
    for it in items:
        output.append({
            "title": it.get("title"),
            "url": it.get("link"),
            "snippet": it.get("snippet")
        })
    return output
