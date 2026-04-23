from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/etablissements", tags=["Etablissements"])

@router.get("/")
def get_all_etablissements(db: Session = Depends(get_db)):
    etablissements = db.query(models.EtablissementProximite).all()
    result = []
    for e in etablissements:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == e.recensement_id).first()
        type_etab = db.query(models.TypeEtablissementProximite).filter(models.TypeEtablissementProximite.id == e.type_etablissement_id).first()
        if recensement and type_etab:
            result.append({
                "recensement_id": e.recensement_id,
                "recensement": recensement,
                "type_etablissement_id": e.type_etablissement_id,
                "type_etablissement": type_etab
            })
    return result

@router.post("/")
def add_etablissement(etablissement: schemas.EtablissementProximiteBase, db: Session = Depends(get_db)):
    db_etablissement = models.EtablissementProximite(**etablissement.dict())
    db.add(db_etablissement)
    db.commit()
    return db_etablissement

@router.delete("/{recensement_id}/{type_etablissement_id}")
def delete_etablissement(recensement_id: int, type_etablissement_id: int, db: Session = Depends(get_db)):
    etablissement = db.query(models.EtablissementProximite).filter(
        models.EtablissementProximite.recensement_id == recensement_id,
        models.EtablissementProximite.type_etablissement_id == type_etablissement_id
    ).first()
    if not etablissement:
        raise HTTPException(status_code=404, detail="Etablissement not found")
    db.delete(etablissement)
    db.commit()
    return {"message": "Etablissement deleted"}