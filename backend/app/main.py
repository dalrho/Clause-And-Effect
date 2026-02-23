from fastapi import FastAPI
from app.api.routes import upload, analyze, simulate

app = FastAPI()

app.include_router(upload.router, prefix="/upload")
app.include_router(analyze.router, prefix="/analyze")
app.include_router(simulate.router, prefix="/simulate")

@app.get("/")
def root():
    return {"message": "Contract Intelligence API running"}