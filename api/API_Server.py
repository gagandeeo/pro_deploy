from fastapi import FastAPI, Depends, HTTPException
from typing import List
from database import SessionLocal, engine
import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api")
def get_home():
    return {"test": "checked"}


@app.post("/api/test-end1")
def test_store_post(request: str, db: Session = Depends(get_db)):
    db_query = models.TestRequest(
        input=request
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return {"input": db_query.input}


@app.get("/api/test-end1")
def test_store_get(db: Session = Depends(get_db)):
    db_query = db.query(models.TestRequest).all()
    return {"history": db_query}
