from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api/organisations", tags=["Organisations"])

@router.get("/")
def get_all_organisations(db: Session = Depends(get_db)):
    organisations = db.query(models.OrganisationAgricole).all()
    result = []
    for o in organisations:
        recensement = db.query(models.Recensement).filter(models.Recensement.id == o.recensement_id).first()
        type_org = db.query(models.TypeOrganisationAgricole).filter(models.TypeOrganisationAgricole.id == o.type_organisation_id).first()
        if recensement and type_org:
            result.append({
                "recensement_id": o.recensement_id,
                "recensement": recensement,
                "type_organisation_id": o.type_organisation_id,
                "type_organisation": type_org
            })
    return result

@router.post("/")
def add_organisation(organisation: schemas.OrganisationAgricoleBase, db: Session = Depends(get_db)):
    db_organisation = models.OrganisationAgricole(**organisation.dict())
    db.add(db_organisation)
    db.commit()
    return db_organisation

@router.delete("/{recensement_id}/{type_organisation_id}")
def delete_organisation(recensement_id: int, type_organisation_id: int, db: Session = Depends(get_db)):
    organisation = db.query(models.OrganisationAgricole).filter(
        models.OrganisationAgricole.recensement_id == recensement_id,
        models.OrganisationAgricole.type_organisation_id == type_organisation_id
    ).first()
    if not organisation:
        raise HTTPException(status_code=404, detail="Organisation not found")
    db.delete(organisation)
    db.commit()
    return {"message": "Organisation deleted"}