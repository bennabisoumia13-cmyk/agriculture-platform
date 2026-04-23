from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/financements", tags=["Financements"])

# READ - جلب جميع التمويلات
@router.get("/", response_model=List[schemas.FinancementDetail])
def get_all_financements(db: Session = Depends(get_db)):
    financements = db.query(models.Financement).all()
    result = []
    for f in financements:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == f.recensement_id).first()
        type_fin = db.query(models.TypeFinancement).filter(models.TypeFinancement.id == f.type_financement_id).first()
        if recensement and type_fin:
            result.append({
                "recensement": recensement,
                "type_financement": type_fin
            })
    return result

# CREATE - إضافة تمويل جديد
@router.post("/", response_model=schemas.Financement)
def add_financement(financement: schemas.FinancementBase, db: Session = Depends(get_db)):
    # التحقق من وجود المزارع
    recensement = db.query(models.Recensement).filter(models.Recensement.id == financement.recensement_id).first()
    if not recensement:
        raise HTTPException(status_code=404, detail="Recensement not found")
    
    # التحقق من وجود نوع التمويل
    type_fin = db.query(models.TypeFinancement).filter(models.TypeFinancement.id == financement.type_financement_id).first()
    if not type_fin:
        raise HTTPException(status_code=404, detail="Type financement not found")
    
    # التحقق من عدم وجود تمويل مكرر
    existing = db.query(models.Financement).filter(
        models.Financement.recensement_id == financement.recensement_id,
        models.Financement.type_financement_id == financement.type_financement_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Financement already exists")
    
    db_financement = models.Financement(**financement.dict())
    db.add(db_financement)
    db.commit()
    return db_financement

# UPDATE - تعديل تمويل موجود
@router.put("/{recensement_id}/{type_financement_id}")
def update_financement(
    recensement_id: int, 
    type_financement_id: int, 
    financement: schemas.FinancementBase, 
    db: Session = Depends(get_db)
):
    # البحث عن التمويل الموجود
    existing = db.query(models.Financement).filter(
        models.Financement.recensement_id == recensement_id,
        models.Financement.type_financement_id == type_financement_id
    ).first()
    
    if not existing:
        raise HTTPException(status_code=404, detail="Financement not found")
    
    # التحقق من وجود المزارع الجديد
    recensement = db.query(models.Recensement).filter(models.Recensement.id == financement.recensement_id).first()
    if not recensement:
        raise HTTPException(status_code=404, detail="New recensement not found")
    
    # التحقق من وجود نوع التمويل الجديد
    type_fin = db.query(models.TypeFinancement).filter(models.TypeFinancement.id == financement.type_financement_id).first()
    if not type_fin:
        raise HTTPException(status_code=404, detail="New type financement not found")
    
    # حذف القديم وإضافة الجديد
    db.delete(existing)
    new_financement = models.Financement(**financement.dict())
    db.add(new_financement)
    db.commit()
    
    return {"message": "Financement updated successfully"}

# DELETE - حذف تمويل
@router.delete("/{recensement_id}/{type_financement_id}")
def delete_financement(
    recensement_id: int, 
    type_financement_id: int, 
    db: Session = Depends(get_db)
):
    # البحث عن التمويل
    financement = db.query(models.Financement).filter(
        models.Financement.recensement_id == recensement_id,
        models.Financement.type_financement_id == type_financement_id
    ).first()
    
    if not financement:
        raise HTTPException(status_code=404, detail="Financement not found")
    
    db.delete(financement)
    db.commit()
    
    return {"message": "Financement deleted successfully"}