<div align="center">

# ⚡ Smart Meeting Assistant

**Drop a meeting transcript. Get a summary, decisions, risks, and action items — in seconds.**

[![Live Demo](https://img.shields.io/badge/Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://kazg3lksqf5svssah3uo2j.streamlit.app)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/anikameenuak/smart-meeting-assistant)
[![Groq](https://img.shields.io/badge/Groq-F54F31?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![LLaMA 3.3](https://img.shields.io/badge/LLaMA_3.3_70B-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://llama.meta.com)
[![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

🔗 **[Try it live →](https://kazg3lksqf5svssah3uo2j.streamlit.app)**

</div>

---

## What it does

Meetings produce noise. Smart Meeting Assistant turns that noise into structured intelligence.

Paste any raw meeting transcript and get back:

- **Summary** — key discussion points, decisions made, and risks identified
- **Action Items** — every task extracted with owner and deadline
- **CSV Export** — download the action table and share with your team instantly

Runs on **LLaMA 3.3 70B** via **Groq** — fast enough to feel instant.

---

## Project Structure

```
smart-meeting-assistant/
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend — /analyze endpoint
├── backend/
│   ├── __init__.py
│   ├── summarizer.py       # generate_summary() — key points, decisions, risks
│   └── extractor.py        # extract_actions() — returns structured JSON task list
├── test_run.py             # Manual testing script (not part of the app)
├── requirements.txt
├── .env                    # API keys — never commit this
└── README.md
```

---

## How it works

```
User pastes transcript
        │
        ▼
  Streamlit (app.py)
        │  POST /analyze
        ▼
  FastAPI (main.py)
        │
        ├──▶ summarizer.py → generate_summary()
        │         └── Groq API (LLaMA 3.3 70B)
        │               └── Key points · Decisions · Risks
        │
        └──▶ extractor.py → extract_actions()
                  └── Groq API (LLaMA 3.3 70B)
                        └── [{ task, owner, deadline }]

        Both results → Streamlit → rendered + downloadable as CSV
```

---

## API

### `POST /analyze`

**Request**
```json
{
  "transcript": "John: We need to finish the dashboard by Friday. Sarah: I will handle the frontend..."
}
```

**Response**
```json
{
  "summary": "## Key Discussion Points\n- Dashboard deadline set for Friday\n\n## Decisions Made\n- Sarah owns frontend, Mike owns API\n\n## Risks\n- Tight deadline with no buffer mentioned",
  "actions": [
    { "task": "Complete frontend", "owner": "Sarah", "deadline": "Friday" },
    { "task": "Prepare the API",   "owner": "Mike",  "deadline": "Friday" }
  ]
}
```

If owner or deadline is not found in the transcript, defaults to `"unknown"` and `"not mentioned"`.

---

## Local Setup

### 1. Clone

```bash
git clone https://github.com/anikameenuak/smart-meeting-assistant.git
cd smart-meeting-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get a free key at [console.groq.com](https://console.groq.com).

### 4. Start the backend

```bash
uvicorn main:app --reload
```

Runs at `http://127.0.0.1:8000`

### 5. Start the frontend

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Requirements

```
streamlit
fastapi
uvicorn
groq
python-dotenv
pandas
requests
```

---

## Deployment

### Frontend — Streamlit Cloud

1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → connect your repo
3. Set entry point: `app.py`
4. Add secret under **Settings → Secrets**:
```
GROQ_API_KEY = "your_key_here"
```

### Backend — Render (free tier)

> ⚠️ Streamlit Cloud cannot reach `localhost:8000`. The FastAPI backend must be deployed separately.

1. Go to [render.com](https://render.com) → New Web Service → connect your repo
2. Build command: `pip install -r requirements.txt`
3. Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Add environment variable: `GROQ_API_KEY`
5. Copy your Render URL and update `app.py`:

```python
# Replace:
response = requests.post("http://127.0.0.1:8000/analyze", ...)

# With:
response = requests.post("https://your-app.onrender.com/analyze", ...)
```

---

## Environment Variables

| Variable | Required | Where to get it |
|---|---|---|
| `GROQ_API_KEY` | ✅ | [console.groq.com](https://console.groq.com) |

---

## .gitignore

```
.env
__pycache__/
*.pyc
.DS_Store
```

---

<div align="center">

Built with ⚡ by [anikameenuak](https://github.com/anikameenuak)

</div>
