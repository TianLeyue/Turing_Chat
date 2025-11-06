# backend/app/main.py
import os
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ 新增
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://host.docker.internal:11434/api")

app = FastAPI(title="Turing Chat - FastAPI + Ollama (qwen3:8b)")

# ✅ 允许前端（localhost:5173）访问后端
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或者仅 ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    system: str | None = None
    stream: bool = False

@app.post("/api/chat")
async def chat(req: ChatRequest):
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "qwen3:8b"),
        "prompt": req.prompt,
        "system": req.system or "",
        "stream": False
    }

    url = f"{OLLAMA_BASE}/generate" if not OLLAMA_BASE.endswith("/generate") else OLLAMA_BASE
    if url.endswith("/api"):
        url = url + "/generate"

    async with httpx.AsyncClient(timeout=600.0) as client:
        try:
            resp = await client.post(url, json=payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {e}")

        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=f"Ollama error: {resp.text}")

        data = resp.json()
        text = data.get("completion") or data.get("response") or resp.text
    return {"reply": text}
