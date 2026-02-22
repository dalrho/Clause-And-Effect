import os
import uuid

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_file(file):
    file_id = str(uuid.uuid4())
    path = f"{UPLOAD_DIR}/{file_id}.pdf"

    with open(path, "wb") as f:
        f.write(file.file.read())
    
    return file_id, path