from fastapi import APIRouter, UploadFile
from app.utils.file_handler import save_file

router = APIRouter()

# python dictionary fake database for demo
# replace later with postgres
fake_db = {}

@router.post("/")
async def upload_contract(file: UploadFile):
    file_id, path = save_file(file)
    fake_db[file_id] = {"path": path}
    return {"contract_id": file_id}