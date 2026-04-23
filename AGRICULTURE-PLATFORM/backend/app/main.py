from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # تأكدي من وجود هذا السطر
import os
from .routers import financements, credits, soutiens, assurances, etablissements, ecoulements, marches, organisations

app = FastAPI(title="Agricultural Statistics Platform - Finance Module")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚠️ هذا هو الجزء المهم - إضافة خدمة الملفات الثابتة
frontend_path = os.path.join(os.path.dirname(__file__), "../../Frontend")
if os.path.exists(frontend_path):
    app.mount("/Frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")
else:
    print(f"Warning: Frontend folder not found at {frontend_path}")

# إضافة جميع الروترات
app.include_router(financements.router)
app.include_router(credits.router)
app.include_router(soutiens.router)
app.include_router(assurances.router)
app.include_router(etablissements.router)
app.include_router(ecoulements.router)
app.include_router(marches.router)
app.include_router(organisations.router)

@app.get("/")
def root():
    return {"message": "Agricultural Statistics Platform - Finance Module API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}