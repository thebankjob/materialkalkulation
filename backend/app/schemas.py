from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class MaterialBase(BaseModel):
    name: str
    einheit: str
    kategorie: Optional[str]
    technische_eigenschaften: Optional[str]

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int
    class Config:
        orm_mode = True

class LieferantBase(BaseModel):
    name: str
    kontaktinfo: Optional[str]

class LieferantCreate(LieferantBase):
    pass

class Lieferant(LieferantBase):
    id: int
    class Config:
        orm_mode = True

class MaterialLieferantBase(BaseModel):
    material_id: int
    lieferant_id: int
    artikelnummer: Optional[str]
    verpackungseinheit: Optional[str]
    kommentar: Optional[str]

class MaterialLieferantCreate(MaterialLieferantBase):
    pass

class MaterialLieferant(MaterialLieferantBase):
    id: int
    class Config:
        orm_mode = True

class PreisBase(BaseModel):
    material_lieferant_id: int
    preis: float
    datum: date
    rechnungsnummer: Optional[str]
    rechnungsdatum: Optional[date]
    notiz: Optional[str]

class PreisCreate(PreisBase):
    pass

class Preis(PreisBase):
    id: int
    class Config:
        orm_mode = True

class AenderungshistorieBase(BaseModel):
    material_lieferant_id: Optional[int]
    aktion: str
    zeitpunkt: date
    benutzer: Optional[str]
    rechnungsnummer: Optional[str]
    rechnungsdatum: Optional[date]
    kommentar: Optional[str]

class AenderungshistorieCreate(AenderungshistorieBase):
    pass

class Aenderungshistorie(AenderungshistorieBase):
    id: int
    class Config:
        orm_mode = True
