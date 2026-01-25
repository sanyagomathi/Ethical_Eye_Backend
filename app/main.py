from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

import os

from app.api.scan import router as scan_router
from app.api.alternatives import router as alternatives_router
from app.api.gemini import router as gemini_router
from app.api.chat import router as chat_router

app = FastAPI(title="Ethical Ingredient Decoder API")

# CORS (allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(scan_router, prefix="/api")
app.include_router(alternatives_router, prefix="/api")
app.include_router(gemini_router, prefix="/api") 
app.include_router(chat_router, prefix="/api")

# Root check
@app.get("/")
def root():
    return {"status": "Ethical Eye backend running"}

@app.get("/api/debug-env")
def debug_env():
    return {
        "has_credentials": bool(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")),
        "credentials_path": os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
        "has_project": bool(os.environ.get("GOOGLE_CLOUD_PROJECT")),
        "project": os.environ.get("GOOGLE_CLOUD_PROJECT"),
        "has_location": bool(os.environ.get("GOOGLE_CLOUD_LOCATION")),
        "location": os.environ.get("GOOGLE_CLOUD_LOCATION"),
    }