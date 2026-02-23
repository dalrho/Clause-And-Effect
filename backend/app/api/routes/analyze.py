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

    pages = extract_text_with_pages(data["path"])
    chunks = chunk_pages(pages)

    # Instead of a loop, send the first 20 chunks as one batch
    # This counts as 1 API call, staying well under the 5 RPM limit
    results = analyze_multiple_clauses(chunks[:20])

    fake_db[contract_id]["analysis"] = results
    return {"contract_id": contract_id, "clauses": results}