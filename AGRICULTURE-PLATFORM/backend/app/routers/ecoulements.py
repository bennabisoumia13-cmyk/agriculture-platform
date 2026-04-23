from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/ecoulements", tags=["Ecoulements"])

@router.get("/")
def get_all_ecoulements(db: Session = Depends(get_db)):
    ecoulements = db.query(models.EcoulementProduit).all()
    result = []
    for e in ecoulements:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == e.recensement_id).first()
        type_ecoulement = db.query(models.TypeEcoulement).filter(models.TypeEcoulement.id == e.type_ecoulement_id).first()
        if recensement and type_ecoulement:
            result.append({
                "recensement_id": e.recensement_id,
                "recensement": recensement,
                "type_ecoulement_id": e.type_ecoulement_id,
                "type_ecoulement": type_ecoulement
            })
    return result

@router.post("/")
def add_ecoulement(ecoulement: schemas.EcoulementProduitBase, db: Session = Depends(get_db)):
    db_ecoulement = models.EcoulementProduit(**ecoulement.dict())
    db.add(db_ecoulement)
    db.commit()
    return db_ecoulement

@router.delete("/{recensement_id}/{type_ecoulement_id}")
def delete_ecoulement(recensement_id: int, type_ecoulement_id: int, db: Session = Depends(get_db)):
    ecoulement = db.query(models.EcoulementProduit).filter(
        models.EcoulementProduit.recensement_id == recensement_id,
        models.EcoulementProduit.type_ecoulement_id == type_ecoulement_id
    ).first()
    if not ecoulement:
        raise HTTPException(status_code=404, detail="Ecoulement not found")
    db.delete(ecoulement)
    db.commit()
    return {"message": "Ecoulement deleted"}