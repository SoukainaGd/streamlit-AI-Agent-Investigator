🕵️‍♀️ AI Agent Investigator
AI Agent Investigator is a Streamlit-based multi-agent system that investigates companies for potential relationships with defense contractors, military suppliers, or activities related to geopolitical conflicts — such as the military invasion in Gaza and the West Bank.

It automates open-source intelligence (OSINT) research using AI agents that search, analyze, and verify publicly available information.

🚀 Features
🔍 Automated OSINT Research — Collects and summarizes public information about a given company.

🤖 Multi-Agent Architecture —

Researcher Agent: Finds and summarizes data from verified sources.

Verifier Agent: Cross-checks claims against multiple primary sources and assigns confidence levels.

🌍 Context Awareness — Focus on military, defense, and geopolitical contexts (e.g., Gaza/West Bank).

📄 JSON Output — Returns clean, structured findings with source citations.

💾 Download Results — Export your investigation as a .json file.

🧠 Example Output
json
￼Copy code
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
⚙️ How It Works
The user enters a company name (e.g., “Nestlé”, “Microsoft”, “L’Oréal”).

The Researcher Agent uses web search tools (SerpAPI) to gather relevant evidence.

The Verifier Agent cross-checks the findings and assigns confidence levels.

The app outputs structured claims and allows exporting results as JSON.

🧩 Tech Stack
Python 3.10+

Streamlit – Interactive UI

CrewAI – Multi-agent orchestration

OpenAI API – LLM reasoning & analysis

SerpAPI – Web search integration

dotenv – Secure API key management

🛠 Setup Instructions (Local)
bash
￼Copy code
# 1. Clone the repository
git clone https://github.com/SoukainaGd/streamlit-AI-Agent-Investigator.git
cd streamlit-AI-Agent-Investigator

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file
OPENAI_API_KEY=your_openai_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here

# 5. Run the app
streamlit run app.py
☁️ Streamlit Cloud Deployment
This app is live on Streamlit Cloud.
You can deploy it yourself by connecting your GitHub repo and setting the secrets in Settings → Secrets:

ini
￼Copy code
OPENAI_API_KEY = "your_openai_api_key_here"
SERPAPI_API_KEY = "your_serpapi_api_key_here"
🧑‍💻 Project Structure
bash
￼Copy code
streamlit-AI-Agent-Investigator/
│
├── agents/
│   ├── researcher_agent.py
│   └── verifier_agent.py
│
├── tools/
│   └── web_search_tool.py
│
├── crew.py              # Multi-agent orchestration logic
├── app.py               # Streamlit front-end
├── requirements.txt
├── .env.example
└── README.md
🧭 Example Use Cases
Investigate if a company has defense contracts

Track partnerships linked to military or surveillance operations

Examine supply chains with geopolitical implications

👩‍💻 Author
Soukaina Gadir
AI & Data Science Researcher | OSINT Automation Enthusiast
📍 GitHub: @SoukainaGd

⚖️ Disclaimer
This tool uses publicly available information and AI-generated analysis.
It does not make legal or definitive claims — always verify results manually.
The purpose of this project is transparency and responsible AI investigation.

✅ To Add It to Your GitHub Repo
In your local project folder, run:

bash
￼Copy code
touch README.md
Then paste the text above into that file, save it, and push:

bash
￼Copy code
git add README.md
git commit -m "docs: add project README"
git push origin main
Would you like me to tailor the top of the README (title + tagline) to sound more academic (for a portfolio / research project), or more professional / product-like (for public users)?

￼
￼
￼
￼
￼
￼
