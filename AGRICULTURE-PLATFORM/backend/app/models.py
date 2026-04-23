from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

# ========== جداول الأنواع (Types) ==========

class TypeFinancement(Base):
    __tablename__ = "type_financement"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeCreditBancaire(Base):
    __tablename__ = "type_credit_bancaire"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeSoutienPublic(Base):
    __tablename__ = "type_soutien_public"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeAssuranceAgricole(Base):
    __tablename__ = "type_assurance_agricole"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeEtablissementProximite(Base):
    __tablename__ = "type_etablissement_proximite"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeEcoulement(Base):
    __tablename__ = "type_ecoulement"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeMarche(Base):
    __tablename__ = "type_marche"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

class TypeOrganisationAgricole(Base):
    __tablename__ = "type_organisation_agricole"
    id = Column(Integer, primary_key=True, index=True)
    nom_fr = Column(String(150))
    nom_ar = Column(String(150))

# ========== الجداول الرئيسية ==========

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

class CreditBancaire(Base):
    __tablename__ = "credit_bancaire"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_credit_id = Column(Integer, ForeignKey("type_credit_bancaire.id"), primary_key=True)

class SoutienPublic(Base):
    __tablename__ = "soutien_public"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_soutien_id = Column(Integer, ForeignKey("type_soutien_public.id"), primary_key=True)

class AssuranceAgricole(Base):
    __tablename__ = "assurances_agricoles"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_assurance_id = Column(Integer, ForeignKey("type_assurance_agricole.id"), primary_key=True)

class EtablissementProximite(Base):
    __tablename__ = "etablissements_proximite"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_etablissement_id = Column(Integer, ForeignKey("type_etablissement_proximite.id"), primary_key=True)

class EcoulementProduit(Base):
    __tablename__ = "ecoulements_produits"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_ecoulement_id = Column(Integer, ForeignKey("type_ecoulement.id"), primary_key=True)

class MarcheProduit(Base):
    __tablename__ = "marches_produits"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_marche_id = Column(Integer, ForeignKey("type_marche.id"), primary_key=True)

class OrganisationAgricole(Base):
    __tablename__ = "organisations_agricoles"
    recensement_id = Column(Integer, ForeignKey("recensements.id"), primary_key=True)
    type_organisation_id = Column(Integer, ForeignKey("type_organisation_agricole.id"), primary_key=True)