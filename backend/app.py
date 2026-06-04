from fastapi import FastAPI
from pydantic import BaseModel

from backend.summarizer import generate_summary
from backend.extractor import extract_actions

app = FastAPI()

# Request format
class MeetingRequest(BaseModel):
    transcript: str


@app.get("/")
def home():
    return {"message": "AI Meeting Assistant API is running"}


@app.post("/analyze")
def analyze_meeting(req: MeetingRequest):

    summary = generate_summary(req.transcript)
    actions = extract_actions(req.transcript)

    return {
        "summary": summary,
        "actions": actions
    }