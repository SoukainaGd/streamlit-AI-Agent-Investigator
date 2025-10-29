# 🕵️‍♀️ AI Agent Investigator

**AI Agent Investigator** is a Streamlit-based multi-agent system that investigates companies for potential relationships with defense contractors, military suppliers, or activities related to geopolitical conflicts — such as the military invasion in **Gaza and the West Bank**.

It automates open-source intelligence (OSINT) research using AI agents that search, analyze, and verify publicly available information.

---

## 🚀 Features

- 🔍 **Automated OSINT Research** — Collects and summarizes public information about a given company.  
- 🤖 **Multi-Agent Architecture**  
  - **Researcher Agent:** Finds and summarizes data from verified sources.  
  - **Verifier Agent:** Cross-checks claims against multiple primary sources and assigns confidence levels.  
- 🌍 **Context Awareness** — Focus on military, defense, and geopolitical contexts (e.g., Gaza/West Bank).  
- 📄 **JSON Output** — Returns clean, structured findings with source citations.  
- 💾 **Download Results** — Export your investigation as a `.json` file.  

---

## 🧠 Example Output

```json
[
  {
    "claim": "Microsoft partnered with Palantir to deliver analytics to classified networks for national security operations.",
    "sources": [
      {
        "url": "https://news.microsoft.com/source/2024/08/08/palantir-and-microsoft-partner-to-deliver-enhanced-analytics-and-ai-services/",
        "excerpt": "Palantir and Microsoft partner to deliver enhanced analytics and AI services for critical national security operations."
      }
    ],
    "confidence": 0.9,
    "timestamp": "2024-08-08T00:00:00Z"
  }
]
