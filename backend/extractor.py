from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def extract_actions(transcript):

    prompt = f"""
Extract action items from this meeting transcript.

Return ONLY valid JSON array like this:
[
  {{
    "task": "",
    "owner": "",
    "deadline": ""
  }}
]

Rules:
- No markdown
- No explanation
- If owner not found → "unknown"
- If deadline not found → "not mentioned"

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    # Convert string → Python object
    return json.loads(content)