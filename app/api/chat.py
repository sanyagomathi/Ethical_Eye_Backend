from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Dict, List

from app.api.gemini import generate_with_gemini

import re


def strip_markdown_json(text: str) -> str:
    """
    Removes ```json ... ``` or ``` ... ``` wrappers if present
    """
    if not text:
        return text

    text = text.strip()

    # Remove ```json or ``` wrappers
    text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE).strip()
    text = re.sub(r"```$", "", text).strip()

    return text


router = APIRouter()

class ChatRequest(BaseModel):
    food: str = Field(..., min_length=1)
    values: Dict[str, bool] = Field(default_factory=dict)

class Alternative(BaseModel):
    name: str
    reason: str
    caution: str | None = None

class ChatResponse(BaseModel):
    explanation: str
    alternatives: List[Alternative]
    follow_up: str

def build_prompt(food: str, values: Dict[str, bool]) -> str:
    constraints = ", ".join(
        [k.replace("_", " ") for k, v in values.items() if v]
    ) or "no specific constraints"

    return f"""
You are an ethical food assistant.

User food item: {food}
User constraints: {constraints}

Rules:
- Suggest food alternatives only
- Be practical and realistic
- Avoid medical claims
- If vegan is true, never suggest dairy, meat, eggs
- If allergen avoidance is implied, mention cautions

Return the response in this exact JSON format:

{{
  "explanation": "...",
  "alternatives": [
    {{
      "name": "...",
      "reason": "...",
      "caution": "..."
    }}
  ],
  "follow_up": "..."
}}
"""
@router.post("/chat/alternatives/raw")
def raw_debug(payload: dict):
    return payload


@router.post("/chat/alternatives", response_model=ChatResponse)
def food_chat(payload: ChatRequest):
    import json

    try:
        prompt = build_prompt(payload.food, payload.values)
        raw = generate_with_gemini(prompt)
        print("GEMINI RAW:", raw)   # 👈 ADD THIS
        cleaned = strip_markdown_json(raw)

        data = json.loads(cleaned)

        return ChatResponse(
            explanation=data.get("explanation", ""),
            alternatives=data.get("alternatives", []),
            follow_up=data.get("follow_up", "")
        )

    except Exception as e:
        # 🔒 ABSOLUTE SAFETY NET — NEVER RETURN NONE
        return ChatResponse(
            explanation="I couldn’t generate alternatives right now. Please try again.",
            alternatives=[],
            follow_up="You can try another food item or adjust your preferences."
        )
