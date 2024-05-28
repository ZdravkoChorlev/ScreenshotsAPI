from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers import health, screenshots
from app.db import mongodb

app = FastAPI(
    summary="Screenshots Service"
)

@app.on_event("startup")
def start_db():
    mongodb.get_database()
    
app.include_router(health.router, prefix="/isalive")
app.include_router(screenshots.router, prefix="/screenshots")

@app.get("/")
def default():
    content = {"version": "0.0.1"}
    return JSONResponse(status_code=200, content=content)
