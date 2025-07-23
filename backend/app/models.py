from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Material(Base):
    __tablename__ = "materialien"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    einheit = Column(String, nullable=False)
    kategorie = Column(String, nullable=True)
    technische_eigenschaften = Column(Text, nullable=True)  # JSON als String

    mappings = relationship("MaterialLieferant", back_populates="material")

class Lieferant(Base):
    __tablename__ = "lieferanten"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    kontaktinfo = Column(String, nullable=True)

    mappings = relationship("MaterialLieferant", back_populates="lieferant")

class MaterialLieferant(Base):
    __tablename__ = "material_lieferant"
    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materialien.id"), nullable=False)
    lieferant_id = Column(Integer, ForeignKey("lieferanten.id"), nullable=False)
    artikelnummer = Column(String, nullable=True)
    verpackungseinheit = Column(String, nullable=True)
    kommentar = Column(String, nullable=True)

    material = relationship("Material", back_populates="mappings")
    lieferant = relationship("Lieferant", back_populates="mappings")
    preise = relationship("Preis", back_populates="mapping")
    historien = relationship("Aenderungshistorie", back_populates="mapping")

class Preis(Base):
    __tablename__ = "preise"
    id = Column(Integer, primary_key=True, index=True)
    material_lieferant_id = Column(Integer, ForeignKey("material_lieferant.id"), nullable=False)
    preis = Column(Float, nullable=False)
    datum = Column(Date, nullable=False)
    rechnungsnummer = Column(String, nullable=True)
    rechnungsdatum = Column(Date, nullable=True)
    notiz = Column(String, nullable=True)

    mapping = relationship("MaterialLieferant", back_populates="preise")

class Aenderungshistorie(Base):
    __tablename__ = "aenderungshistorie"
    id = Column(Integer, primary_key=True, index=True)
    material_lieferant_id = Column(Integer, ForeignKey("material_lieferant.id"), nullable=True)
    aktion = Column(String, nullable=False)
    zeitpunkt = Column(Date, nullable=False)
    benutzer = Column(String, nullable=True)
    rechnungsnummer = Column(String, nullable=True)
    rechnungsdatum = Column(Date, nullable=True)
    kommentar = Column(String, nullable=True)

    mapping = relationship("MaterialLieferant", back_populates="historien")
