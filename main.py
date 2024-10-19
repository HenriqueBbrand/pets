from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# Montar diretório de templates
templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "app/templates"))

app = FastAPI()

# Montar diretório estático
app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "app/static")), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, port=8888)
