from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/marches", tags=["Marches"])

@router.get("/")
def get_all_marches(db: Session = Depends(get_db)):
    marches = db.query(models.MarcheProduit).all()
    result = []
    for m in marches:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == m.recensement_id).first()
        type_marche = db.query(models.TypeMarche).filter(models.TypeMarche.id == m.type_marche_id).first()
        if recensement and type_marche:
            result.append({
                "recensement_id": m.recensement_id,
                "recensement": recensement,
                "type_marche_id": m.type_marche_id,
                "type_marche": type_marche
            })
    return result

@router.post("/")
def add_marche(marche: schemas.MarcheProduitBase, db: Session = Depends(get_db)):
    db_marche = models.MarcheProduit(**marche.dict())
    db.add(db_marche)
    db.commit()
    return db_marche

@router.delete("/{recensement_id}/{type_marche_id}")
def delete_marche(recensement_id: int, type_marche_id: int, db: Session = Depends(get_db)):
    marche = db.query(models.MarcheProduit).filter(
        models.MarcheProduit.recensement_id == recensement_id,
        models.MarcheProduit.type_marche_id == type_marche_id
    ).first()
    if not marche:
        raise HTTPException(status_code=404, detail="Marche not found")
    db.delete(marche)
    db.commit()
    return {"message": "Marche deleted"}