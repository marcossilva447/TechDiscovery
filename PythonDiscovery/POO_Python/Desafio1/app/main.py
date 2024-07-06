from fastapi import FastAPI, HTTPException, Query
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/atleta/", response_model=schemas.Atleta)
def create_atleta(atleta: schemas.AtletaCreate, db: Session = SessionLocal()):
    try:
        return crud.create_atleta(db=db, atleta=atleta)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")

@app.get("/atleta/", response_model=Page[schemas.Atleta])
def read_atletas(nome: Optional[str] = None, db: Session = SessionLocal()):
    atletas = crud.get_atletas(db, nome=nome)
    return paginate(atletas)

@app.get("/atleta/{atleta_id}", response_model=schemas.Atleta)
def read_atleta(atleta_id: int, db: Session = SessionLocal()):
    db_atleta = crud.get_atleta(db, atleta_id=atleta_id)
    if db_atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return db_atleta

add_pagination(app)
