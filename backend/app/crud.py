from sqlalchemy.orm import Session
from . import models, schemas

# MATERIALIEN
def get_materialien(db: Session):
    return db.query(models.Material).all()

def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

# LIEFERANTEN
def get_lieferanten(db: Session):
    return db.query(models.Lieferant).all()

def create_lieferant(db: Session, lieferant: schemas.LieferantCreate):
    db_lieferant = models.Lieferant(**lieferant.dict())
    db.add(db_lieferant)
    db.commit()
    db.refresh(db_lieferant)
    return db_lieferant

# MATERIAL-LIEFERANT
def get_material_lieferant(db: Session):
    return db.query(models.MaterialLieferant).all()

def create_material_lieferant(db: Session, data: schemas.MaterialLieferantCreate):
    db_map = models.MaterialLieferant(**data.dict())
    db.add(db_map)
    db.commit()
    db.refresh(db_map)
    return db_map

# PREISE
def get_preise(db: Session):
    return db.query(models.Preis).all()

def create_preis(db: Session, preis: schemas.PreisCreate):
    db_preis = models.Preis(**preis.dict())
    db.add(db_preis)
    db.commit()
    db.refresh(db_preis)
    return db_preis

# HISTORIE
def get_aenderungshistorie(db: Session):
    return db.query(models.Aenderungshistorie).all()

def create_aenderungshistorie(db: Session, hist: schemas.AenderungshistorieCreate):
    db_hist = models.Aenderungshistorie(**hist.dict())
    db.add(db_hist)
    db.commit()
    db.refresh(db_hist)
    return db_hist
