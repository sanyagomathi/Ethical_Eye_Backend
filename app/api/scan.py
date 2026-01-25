# app/api/scan.py

from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from typing import Dict
import os

import json

from google.cloud import vision
from app.rules import detect_flags

router = APIRouter()

class ScanTextRequest(BaseModel):
    text: str
    values: Dict[str, bool]

def ocr_image(image_bytes: bytes) -> str:
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_bytes)
    response = client.document_text_detection(image=image)
    return response.full_text_annotation.text

@router.post("/scan-text")
def scan_text(payload: ScanTextRequest):
    flags = detect_flags(payload.text, payload.values)
    return {"text": payload.text, "flags": flags}

@router.post("/scan")
async def scan_image(
    image: UploadFile = File(...),
    values: str = Form("{}")   # ✅ IMPORTANT
):
    image_bytes = await image.read()
    values_dict = json.loads(values)

    text = ocr_image(image_bytes)
    flags = detect_flags(text, values_dict)
    return {"text": text, "flags": flags}
