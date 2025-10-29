# crew.py
import json
import time
from crewai import Task, Crew
from agents.researcher_agent import researcher_agent, research_tool
from agents.verifier_agent import verifier_agent


# --- Helper: safe LLM retry wrapper ---
def safe_kickoff(crew, retries=3, delay=10):
    """Retries the Crew kickoff if the LLM hits a Groq rate limit."""
    for attempt in range(retries):
        try:
            return crew.kickoff()
        except Exception as e:
            err = str(e).lower()
            if "rate limit" in err or "rate_limit_exceeded" in err:
                wait = delay * (2 ** attempt)
                print(f"⚠️ Rate limit hit — retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("❌ Crew kickoff failed after retries due to rate limits or other errors.")


# --- Main investigation function ---
def run_investigation(company_name):
    # 🧠 Build focused search query
    query = f"{company_name} contracts Gaza procurement defense site:gov OR site:pdf OR site:news"

    # 💡 Reduce to fewer results to stay under token limits
    evidence = research_tool.func(query, top=3)

    # 🧠 Prompt for structured analysis
    analysis_prompt = f"""
    You are an investigative AI assistant.

    You have access to a list of verified web search results related to "{company_name}".
    Using these summaries, extract factual, verifiable claims about:
    - relationships with other companies or contractors,
    - contracts, procurement, or defense-related activities,
    - geographic or political relevance (especially Gaza/West Bank).

    Be concise and analytical.

    Respond ONLY in valid JSON with this structure:
    [
      {{
        "claim": "text of the claim",
        "sources": [{{"url": "...", "excerpt": "..."}}],
        "confidence": float (0–1),
        "timestamp": "ISO 8601"
      }}
    ]

    Summaries of evidence (for context only):
    {json.dumps([{"title": e["title"], "url": e["url"]} for e in evidence], indent=2)}
    """

    task = Task(
        description=analysis_prompt,
        expected_output="A JSON list of structured claims about the company's relationships, suppliers, and contracts, "
                        "each with fields: claim, sources, confidence, and timestamp.",
        agent=researcher_agent,
    )

    crew = Crew(
        agents=[researcher_agent],
        tasks=[task],
    )

    # 🚀 Safe kickoff with retry logic
    results = safe_kickoff(crew)

    claims_verified = results

    # 💾 Save structured JSON results
    with open(f"{company_name}_investigation.json", "w", encoding="utf-8") as f:
        json.dump(
            claims_verified.raw if hasattr(claims_verified, "raw") else claims_verified,
            f,
            indent=2,
            ensure_ascii=False
        )

    return claims_verified


if __name__ == "__main__":
    company = "Example Company PLC"
    result = run_investigation(company)
    print(result)
