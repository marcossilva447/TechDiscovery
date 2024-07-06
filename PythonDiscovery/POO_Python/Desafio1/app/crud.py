from sqlalchemy.orm import Session
from . import models, schemas

def get_atleta(db: Session, atleta_id: int):
    return db.query(models.Atleta).filter(models.Atleta.id == atleta_id).first()

def get_atletas(db: Session, nome: Optional[str] = None):
    query = db.query(models.Atleta)
    if nome:
        query = query.filter(models.Atleta.nome == nome)
    return query.all()

def create_atleta(db: Session, atleta: schemas.AtletaCreate):
    db_atleta = models.Atleta(
        nome=atleta.nome, 
        cpf=atleta.cpf,
        centro_treinamento=atleta.centro_treinamento,
        categoria=atleta.categoria
    )
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta
