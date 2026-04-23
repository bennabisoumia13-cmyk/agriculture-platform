from pydantic import BaseModel
from typing import Optional

# ========== SCHÉMAS POUR RECENSEMENT ==========
class RecensementBase(BaseModel):
    nom_exploitant: str
    prenom: str
    wilaya: str
    commune: str

class Recensement(RecensementBase):
    id: int
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR TYPE_FINANCEMENT ==========
class TypeFinancementBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeFinancement(TypeFinancementBase):
    id: int
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR FINANCEMENT ==========
class FinancementBase(BaseModel):
    recensement_id: int
    type_financement_id: int

class Financement(FinancementBase):
    class Config:
        from_attributes = True

class FinancementDetail(BaseModel):
    recensement: Recensement
    type_financement: TypeFinancement
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR CREDIT BANCAIRE ==========
class TypeCreditBancaireBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeCreditBancaire(TypeCreditBancaireBase):
    id: int
    class Config:
        from_attributes = True

class CreditBancaireBase(BaseModel):
    recensement_id: int
    type_credit_id: int

class CreditBancaire(CreditBancaireBase):
    class Config:
        from_attributes = True

class CreditDetail(BaseModel):
    recensement: Recensement
    type_credit: TypeCreditBancaire
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR SOUTIEN PUBLIC ==========
class TypeSoutienPublicBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeSoutienPublic(TypeSoutienPublicBase):
    id: int
    class Config:
        from_attributes = True

class SoutienPublicBase(BaseModel):
    recensement_id: int
    type_soutien_id: int

class SoutienPublic(SoutienPublicBase):
    class Config:
        from_attributes = True

class SoutienDetail(BaseModel):
    recensement: Recensement
    type_soutien: TypeSoutienPublic
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR ASSURANCE AGRICOLE ==========
class TypeAssuranceAgricoleBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeAssuranceAgricole(TypeAssuranceAgricoleBase):
    id: int
    class Config:
        from_attributes = True

class AssuranceAgricoleBase(BaseModel):
    recensement_id: int
    type_assurance_id: int

class AssuranceAgricole(AssuranceAgricoleBase):
    class Config:
        from_attributes = True

class AssuranceDetail(BaseModel):
    recensement: Recensement
    type_assurance: TypeAssuranceAgricole
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR ETABLISSEMENT PROXIMITE ==========
class TypeEtablissementProximiteBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeEtablissementProximite(TypeEtablissementProximiteBase):
    id: int
    class Config:
        from_attributes = True

class EtablissementProximiteBase(BaseModel):
    recensement_id: int
    type_etablissement_id: int

class EtablissementProximite(EtablissementProximiteBase):
    class Config:
        from_attributes = True

class EtablissementDetail(BaseModel):
    recensement: Recensement
    type_etablissement: TypeEtablissementProximite
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR ECOULEMENT ==========
class TypeEcoulementBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeEcoulement(TypeEcoulementBase):
    id: int
    class Config:
        from_attributes = True

class EcoulementProduitBase(BaseModel):
    recensement_id: int
    type_ecoulement_id: int

class EcoulementProduit(EcoulementProduitBase):
    class Config:
        from_attributes = True

class EcoulementDetail(BaseModel):
    recensement: Recensement
    type_ecoulement: TypeEcoulement
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR MARCHE ==========
class TypeMarcheBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeMarche(TypeMarcheBase):
    id: int
    class Config:
        from_attributes = True

class MarcheProduitBase(BaseModel):
    recensement_id: int
    type_marche_id: int

class MarcheProduit(MarcheProduitBase):
    class Config:
        from_attributes = True

class MarcheDetail(BaseModel):
    recensement: Recensement
    type_marche: TypeMarche
    class Config:
        from_attributes = True

# ========== SCHÉMAS POUR ORGANISATION AGRICOLE ==========
class TypeOrganisationAgricoleBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeOrganisationAgricole(TypeOrganisationAgricoleBase):
    id: int
    class Config:
        from_attributes = True

class OrganisationAgricoleBase(BaseModel):
    recensement_id: int
    type_organisation_id: int

class OrganisationAgricole(OrganisationAgricoleBase):
    class Config:
        from_attributes = True

class OrganisationDetail(BaseModel):
    recensement: Recensement
    type_organisation: TypeOrganisationAgricole
    class Config:
        from_attributes = True