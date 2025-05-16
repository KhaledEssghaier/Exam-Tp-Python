from fastapi import FastAPI, Depends, HTTPException ,status
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from . import models, schemas
from .database import Base, engine, SessionLocal
from .langchain_utils import get_summary_llm
from typing import Optional

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/", response_model=schemas.MoviePublic)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = models.Movie(title=movie.title, year=movie.year, director=movie.director)
    db.add(db_movie)
    db.commit()  # Important pour générer un ID
    db.refresh(db_movie)

    for actor in movie.actors:
        db_actor = models.Actor(actor_name=actor.actor_name, movie_id=db_movie.id)
        db.add(db_actor)
    db.commit()

    db.refresh(db_movie)
    return db_movie

@app.get("/movies/random/", response_model=schemas.MoviePublic)
def get_random_movie(db: Session = Depends(get_db)):
    movie = db.query(models.Movie).options(joinedload(models.Movie.actors)).order_by(func.random()).first()
    if not movie:
        raise HTTPException(status_code=404, detail="No movies found")
    return movie

@app.post("/generate_summary/", response_model=schemas.SummaryResponse)
def generate_summary(request: schemas.SummaryRequest, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).options(joinedload(models.Movie.actors)).filter(models.Movie.id == request.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    summary_text = get_summary_llm(movie)
    return {"summary_text": summary_text}