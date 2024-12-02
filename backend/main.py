from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from .database import get_db, engine, Base
from .models import User, Program
from .schemas import UserCreate, ProgramCreate
from .auth import create_access_token, get_current_user
from .recommendation_engine import RecommendationEngine
from .crud import create_user, create_program

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return {"id": db_user.id, "email": db_user.email}

@app.post("/admin/upload-program")
def upload_program(
    program: ProgramCreate, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_program = create_program(db, program)
    return db_program

@app.get("/recommendations")
def get_recommendations(
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    rec_engine = RecommendationEngine(db)
    recommended_program_ids = rec_engine.get_recommendations(current_user)
    
    recommended_programs = db.query(Program).filter(Program.id.in_(recommended_program_ids)).all()
    return recommended_programs
