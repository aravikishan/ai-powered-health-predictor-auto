from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import sqlite3
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
conn = sqlite3.connect('health_predictor.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_health_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    weight REAL,
    height REAL,
    medical_history TEXT,
    lifestyle_factors TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS health_tips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
''')

# Seed data
cursor.execute("INSERT INTO health_tips (title, content) VALUES (?, ?)",
               ("Stay Hydrated", "Drink at least 8 glasses of water a day."))
conn.commit()
conn.close()

# Data models
class UserHealthData(BaseModel):
    age: int
    weight: float
    height: float
    medical_history: str
    lifestyle_factors: str

class PredictionResult(BaseModel):
    risk_level: str
    recommendations: List[str]

class HealthTip(BaseModel):
    title: str
    content: str

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict", response_class=HTMLResponse)
async def read_predict(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})

@app.post("/api/predict")
async def predict(user_data: UserHealthData):
    # Mock prediction logic
    risk_level = "Low" if user_data.age < 40 else "High"
    recommendations = ["Exercise regularly", "Maintain a balanced diet"]
    return PredictionResult(risk_level=risk_level, recommendations=recommendations)

@app.get("/recommendations", response_class=HTMLResponse)
async def read_recommendations(request: Request):
    return templates.TemplateResponse("recommendations.html", {"request": request})

@app.get("/api/recommendations")
async def get_recommendations():
    # Mock recommendations
    return ["Exercise regularly", "Maintain a balanced diet"]

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/api/health-tips")
async def get_health_tips():
    conn = sqlite3.connect('health_predictor.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM health_tips")
    tips = cursor.fetchall()
    conn.close()
    return [HealthTip(title=tip[0], content=tip[1]) for tip in tips]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
