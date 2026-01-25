# app/api/alternatives.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List, Any

router = APIRouter()

class AlternativesRequest(BaseModel):
    extracted_text: str
    flags: List[Dict[str, Any]]
    values: Dict[str, bool]

@router.post("/alternatives")
def alternatives(payload: AlternativesRequest):
    suggestions = []

    if payload.values.get("environmental"):
        if any(f["term"] == "palm oil" for f in payload.flags):
            suggestions.append({
                "name": "Palm-oil-free alternative",
                "note": "Look for RSPO-certified or palm-oil-free brands.",
            })

    if payload.values.get("vegan"):
        suggestions.append({
            "name": "Certified vegan option",
            "note": "Check for V-Label or vegan certification.",
        })

    if not suggestions:
        suggestions.append({
            "name": "No clear alternatives found",
            "note": "Try adjusting preferences.",
        })

    return {"alternatives": suggestions}
