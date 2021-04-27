from fastapi import APIRouter, File, UploadFile, HTTPException
import pandas as pd

router = APIRouter(prefix="/admin")


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type == "text/csv":
        entries = pd.read_csv(file.file, sep=";")
        return {"struct:", entries}
    else:
        return HTTPException(
            status_code=415, detail="File must have text/csv MIME type."
        )
