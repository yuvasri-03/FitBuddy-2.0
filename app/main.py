from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import text

from app.database import engine, Base
from app import models
from fastapi import Form
from fastapi.responses import HTMLResponse
from app.ai_service import generate_fitness_plan

app = FastAPI(
title="FitBuddy 2.0",
description="Personalized Fitness Planning and Progress Tracking",
version="2.0.0",
)

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app.mount(
"/static",
StaticFiles(directory=str(BASE_DIR / "static")),
name="static",
)

Base.metadata.create_all(bind=engine)

@app.get("/") 
def home(request: Request):
    return  templates.TemplateResponse(
    request=request,
   name="index.html",
   context={"title": "FitBuddy 2.0"},


)
@app.post("/generate", response_class=HTMLResponse)
def generate_plan(
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    goal: str = Form(...),
    level: str = Form(...),
    diet: str = Form(...),
):
    from html import escape

    safe_name = escape(name)

    try:
        plan = generate_fitness_plan(
            name=name,
            age=age,
            gender=gender,
            goal=goal,
            level=level,
            diet=diet,
        )

        safe_plan = escape(plan).replace("\n", "<br>")

    except Exception as exc:
        print(f"Gemini generation failed: {exc}")
        raise
        safe_plan = (
            "Sorry, we could not generate your plan right now. "
            "Please check your API configuration and try again."
        )

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your FitBuddy AI Plan</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <main class="planner">
            <p class="eyebrow">YOUR AI FITNESS PLAN</p>
            <h1>Hello, {safe_name}!</h1>
            <h2>Your Personalized Plan</h2>
            <section class="plan-content">{safe_plan}</section>
            <a href="/" class="primary-button">Back to Home</a>
        </main>
    </body>
    </html>
    """


@app.get("/health")
def health_check():
  with engine.connect() as connection:
    connection.execute(text("SELECT 1"))

  return {
    "status": "healthy",
    "database": "connected",
}