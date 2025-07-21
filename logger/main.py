# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()

logs: List[str] = []

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/log")
async def receive_log(request: Request):
    data = await request.json()
    logs.append(data["log"])
    return {"status": "ok"}

@app.get("/logs")
async def get_logs():
    return logs

# delete all logs
@app.delete("/logs")
async def delete_logs():
    logs.clear()
    return {"status": "ok"}
@app.get("/")
async def root():
    return {"message": "lloger service is running!"}

@app.get("/logs/shows", response_class=HTMLResponse)
async def serve_log_viewer():
    file_path = os.path.join(os.path.dirname(__file__), "html/index.html")
    return FileResponse(file_path)