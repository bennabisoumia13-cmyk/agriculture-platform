from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import financements

app = FastAPI(title="Agricultural Statistics Platform - Finance Module")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(financements.router)

@app.get("/")
def root():
    return {"message": "Agricultural Statistics Platform - Finance Module API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}