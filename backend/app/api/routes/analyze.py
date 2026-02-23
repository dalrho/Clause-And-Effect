from fastapi import APIRouter, HTTPException
from app.services.ocr import extract_text_with_pages
from app.services.chunking import chunk_pages
from app.services.analyzer import analyze_multiple_clauses
from app.core.db import fake_db

router = APIRouter()


@router.post("/{contract_id}")
def analyze(contract_id: str):
    data = fake_db.get(contract_id)
    if not data:
        raise HTTPException(status_code=404, detail="Contract not found")

    # Pass the file path directly to our new semantic chunker
    chunks = chunk_pages(data["path"])

    # Since we grouped logically, the total chunks will likely be < 15
    results = analyze_multiple_clauses(chunks)

    fake_db[contract_id]["analysis"] = results
    return {"contract_id": contract_id, "clauses": results}