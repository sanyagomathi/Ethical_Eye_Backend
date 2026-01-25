# app/api/gemini.py

from fastapi import APIRouter, HTTPException
import os

router = APIRouter()

def get_gemini_client():
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION")
    use_vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI")

    if not project:
        raise RuntimeError("GOOGLE_CLOUD_PROJECT is missing")
    if not location:
        raise RuntimeError("GOOGLE_CLOUD_LOCATION is missing")
    if str(use_vertex).lower() not in ("true", "1", "yes"):
        raise RuntimeError("GOOGLE_GENAI_USE_VERTEXAI must be True")

    from google import genai
    from google.genai.types import HttpOptions

    return genai.Client(
        http_options=HttpOptions(api_version="v1")
    )

def generate_with_gemini(prompt: str) -> str:
    client = get_gemini_client()
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return resp.text.strip()

@router.get("/gemini-test")
def gemini_test():
    try:
        reply = generate_with_gemini("Reply with exactly: Gemini is working.")
        return {"ok": True, "reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
