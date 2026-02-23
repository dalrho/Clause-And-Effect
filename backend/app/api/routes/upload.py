from fastapi import APIRouter, UploadFile
from app.utils.file_handler import save_file
from app.core.db import fake_db

router = APIRouter()

# python dictionary fake database for demo
# replace later with postgres

@router.post("/")
async def upload_contract(file: UploadFile):
    file_id, path = save_file(file)
    fake_db[file_id] = {"path": path}
    return {"contract_id": file_id}