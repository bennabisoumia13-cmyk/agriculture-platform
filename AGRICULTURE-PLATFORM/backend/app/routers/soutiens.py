from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/soutiens", tags=["Soutiens"])

@router.get("/")
def get_all_soutiens(db: Session = Depends(get_db)):
    soutiens = db.query(models.SoutienPublic).all()
    result = []
    for s in soutiens:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == s.recensement_id).first()
        type_soutien = db.query(models.TypeSoutienPublic).filter(models.TypeSoutienPublic.id == s.type_soutien_id).first()
        if recensement and type_soutien:
            result.append({
                "recensement_id": s.recensement_id,
                "recensement": recensement,
                "type_soutien_id": s.type_soutien_id,
                "type_soutien": type_soutien
            })
    return result

@router.post("/")
def add_soutien(soutien: schemas.SoutienPublicBase, db: Session = Depends(get_db)):
    db_soutien = models.SoutienPublic(**soutien.dict())
    db.add(db_soutien)
    db.commit()
    return db_soutien

@router.delete("/{recensement_id}/{type_soutien_id}")
def delete_soutien(recensement_id: int, type_soutien_id: int, db: Session = Depends(get_db)):
    soutien = db.query(models.SoutienPublic).filter(
        models.SoutienPublic.recensement_id == recensement_id,
        models.SoutienPublic.type_soutien_id == type_soutien_id
    ).first()
    if not soutien:
        raise HTTPException(status_code=404, detail="Soutien not found")
    db.delete(soutien)
    db.commit()
    return {"message": "Soutien deleted"}