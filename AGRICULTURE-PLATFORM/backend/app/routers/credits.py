from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/credits", tags=["Credits"])

@router.get("/")
def get_all_credits(db: Session = Depends(get_db)):
    credits = db.query(models.CreditBancaire).all()
    result = []
    for c in credits:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == c.recensement_id).first()
        type_credit = db.query(models.TypeCreditBancaire).filter(models.TypeCreditBancaire.id == c.type_credit_id).first()
        if recensement and type_credit:
            result.append({
                "recensement_id": c.recensement_id,
                "recensement": recensement,
                "type_credit_id": c.type_credit_id,
                "type_credit": type_credit
            })
    return result

@router.post("/")
def add_credit(credit: schemas.CreditBancaireBase, db: Session = Depends(get_db)):
    db_credit = models.CreditBancaire(**credit.dict())
    db.add(db_credit)
    db.commit()
    return db_credit

@router.delete("/{recensement_id}/{type_credit_id}")
def delete_credit(recensement_id: int, type_credit_id: int, db: Session = Depends(get_db)):
    credit = db.query(models.CreditBancaire).filter(
        models.CreditBancaire.recensement_id == recensement_id,
        models.CreditBancaire.type_credit_id == type_credit_id
    ).first()
    if not credit:
        raise HTTPException(status_code=404, detail="Credit not found")
    db.delete(credit)
    db.commit()
    return {"message": "Credit deleted"}