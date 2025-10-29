# 🕵️‍♀️ AI Agent Investigator

### 🔍 Overview

**AI Agent Investigator** is a Streamlit-based multi-agent OSINT system that investigates companies for potential relationships with defense contractors, military suppliers, or activities related to geopolitical conflicts — such as the military invasion in **Gaza and the West Bank**.

It automates **open-source intelligence (OSINT)** research using AI agents that search, analyze, and verify publicly available information.

---

### 🧩 What’s Included

* Automated **OSINT research** using AI agents
* **Researcher Agent** → finds and summarizes verified public data
* **Verifier Agent** → cross-checks claims and assigns confidence levels
* Context focus on **defense, military, and geopolitical links**
* Outputs results as structured **JSON**
* Export findings as downloadable `.json` reports

---

### ⚙️ How It Works

1. The user enters a company name (e.g., `Nestlé`, `Microsoft`, `L’Oréal`).
2. The **Researcher Agent** searches the web (via SerpAPI) for public reports and documents.
3. The **Verifier Agent** checks evidence across multiple primary sources.
4. The system generates structured claims and confidence scores.
5. Results are displayed in Streamlit and can be downloaded as JSON.

---

### 🧠 Example Output

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
```

---

### 🧰 Tech Stack

 **Python 3.10+**
 **Streamlit** — interactive web app interface
 **CrewAI** — multi-agent orchestration
 **OpenAI API** — LLM reasoning & analysis
 **SerpAPI** — web search integration
 **dotenv** — secure API key management

---

### 🛠 Setup Instructions (Local)

**1. Clone the repository**

```bash
git clone https://github.com/SoukainaGd/streamlit-AI-Agent-Investigator.git
cd streamlit-AI-Agent-Investigator
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create a `.env` file**

```bash
OPENAI_API_KEY=your_openai_api_key_here  
SERPAPI_API_KEY=your_serpapi_api_key_here
```

**5. Run the app**

```bash
streamlit run app.py
```

---

### ☁️ Streamlit Cloud Deployment

1. Connect your GitHub repo to Streamlit Cloud.
2. Go to **Settings → Secrets** and add your keys:

   ```
   OPENAI_API_KEY = your_openai_api_key_here  
   SERPAPI_API_KEY = your_serpapi_api_key_here
   ```
3. Streamlit will auto-deploy your app from `app.py`.

---

### 🧭 Example Use Cases

* Investigate if a company has **defense contracts**
* Track partnerships linked to **military or surveillance** operations
* Examine **supply chains** with geopolitical implications

---

### 👩‍💻 Author

**Soukaina Gadir**
AI & Data Science Researcher
📍 [GitHub: @SoukainaGd](https://github.com/SoukainaGd)

---

### ⚖️ Disclaimer

This tool uses publicly available information and AI-generated analysis.
It does **not** make legal or definitive claims — always verify results manually.
The purpose of this project is **transparency and responsible AI investigation**.


