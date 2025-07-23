from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Materialkalkulation API", version="1.0")

# Dependency für DB-Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Materialkalkulation API läuft!"}

# Materialien CRUD
@app.get("/materialien", response_model=list[schemas.Material])
def get_materialien(db: Session = Depends(get_db)):
    return crud.get_materialien(db)

@app.post("/materialien", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return crud.create_material(db, material)

# Lieferanten CRUD
@app.get("/lieferanten", response_model=list[schemas.Lieferant])
def get_lieferanten(db: Session = Depends(get_db)):
    return crud.get_lieferanten(db)

@app.post("/lieferanten", response_model=schemas.Lieferant)
def create_lieferant(lieferant: schemas.LieferantCreate, db: Session = Depends(get_db)):
    return crud.create_lieferant(db, lieferant)

# Material-Lieferant Mapping
@app.get("/material_lieferant", response_model=list[schemas.MaterialLieferant])
def get_material_lieferant(db: Session = Depends(get_db)):
    return crud.get_material_lieferant(db)

@app.post("/material_lieferant", response_model=schemas.MaterialLieferant)
def create_material_lieferant(data: schemas.MaterialLieferantCreate, db: Session = Depends(get_db)):
    return crud.create_material_lieferant(db, data)

# Preise
@app.get("/preise", response_model=list[schemas.Preis])
def get_preise(db: Session = Depends(get_db)):
    return crud.get_preise(db)

@app.post("/preise", response_model=schemas.Preis)
def create_preis(preis: schemas.PreisCreate, db: Session = Depends(get_db)):
    return crud.create_preis(db, preis)

# Änderungshistorie
@app.get("/aenderungshistorie", response_model=list[schemas.Aenderungshistorie])
def get_aenderungshistorie(db: Session = Depends(get_db)):
    return crud.get_aenderungshistorie(db)

@app.post("/aenderungshistorie", response_model=schemas.Aenderungshistorie)
def create_aenderungshistorie(hist: schemas.AenderungshistorieCreate, db: Session = Depends(get_db)):
    return crud.create_aenderungshistorie(db, hist)
