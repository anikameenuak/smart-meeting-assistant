from backend.summarizer import generate_summary

transcript = """
John: We need to finish the dashboard by Friday.
Sarah: I will complete the frontend.
Mike: I will prepare the API.
"""

summary = generate_summary(transcript)

print(summary)