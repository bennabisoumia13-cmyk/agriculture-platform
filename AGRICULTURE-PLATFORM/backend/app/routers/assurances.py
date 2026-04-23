from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/assurances", tags=["Assurances"])

@router.get("/")
def get_all_assurances(db: Session = Depends(get_db)):
    assurances = db.query(models.AssuranceAgricole).all()
    result = []
    for a in assurances:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == a.recensement_id).first()
        type_assurance = db.query(models.TypeAssuranceAgricole).filter(models.TypeAssuranceAgricole.id == a.type_assurance_id).first()
        if recensement and type_assurance:
            result.append({
                "recensement_id": a.recensement_id,
                "recensement": recensement,
                "type_assurance_id": a.type_assurance_id,
                "type_assurance": type_assurance
            })
    return result

@router.post("/")
def add_assurance(assurance: schemas.AssuranceAgricoleBase, db: Session = Depends(get_db)):
    db_assurance = models.AssuranceAgricole(**assurance.dict())
    db.add(db_assurance)
    db.commit()
    return db_assurance

@router.delete("/{recensement_id}/{type_assurance_id}")
def delete_assurance(recensement_id: int, type_assurance_id: int, db: Session = Depends(get_db)):
    assurance = db.query(models.AssuranceAgricole).filter(
        models.AssuranceAgricole.recensement_id == recensement_id,
        models.AssuranceAgricole.type_assurance_id == type_assurance_id
    ).first()
    if not assurance:
        raise HTTPException(status_code=404, detail="Assurance not found")
    db.delete(assurance)
    db.commit()
    return {"message": "Assurance deleted"}