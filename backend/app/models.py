from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class TypeFinancement(Base):
    __tablename__ = "type_financement"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class Recensement(Base):
    __tablename__ = "recensements"
    id = Column(Integer, primary_key=True, index=True)
    nom_exploitant = Column(String(100))
    prenom = Column(String(100))
    wilaya = Column(String(100))
    commune = Column(String(100))

class Financement(Base):
    __tablename__ = "financements"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_financement_id = Column(Integer, ForeignKey("type_financement.id"), primary_key=True)