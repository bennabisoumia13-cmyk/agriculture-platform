from pydantic import BaseModel

class TypeFinancementBase(BaseModel):
    nom_fr: str
    nom_ar: str

class TypeFinancement(TypeFinancementBase):
    id: int
    class Config:
        orm_mode = True

class RecensementBase(BaseModel):
    nom_exploitant: str
    prenom: str
    wilaya: str
    commune: str

class Recensement(RecensementBase):
    id: int
    class Config:
        orm_mode = True

class FinancementBase(BaseModel):
    recensement_id: int
    type_financement_id: int

class Financement(FinancementBase):
    class Config:
        orm_mode = True

class FinancementDetail(BaseModel):
    recensement: Recensement
    type_financement: TypeFinancement