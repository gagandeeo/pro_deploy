from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import String
from typing import List
from database import SessionLocal, engine
import models
from schemas import TestInfo
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api")
def get_home():
    return {"test": "checked"}


@app.post("/api/test-end")
async def test_store_post(request: TestInfo, db: Session = Depends(get_db)):
    db_query = models.TestRequest(
        input=request.input
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return {"input": db_query.input}


@app.get("/api/test-end")
def test_store_get(db: Session = Depends(get_db)):
    db_query = db.query(models.TestRequest).all()
    return {"history": db_query}
