# teste.py

from fastapi import APIRouter, UploadFile, File
from tasks import app, get_load_tasks

router = APIRouter()


@router.post("/model/load")
async def read_load(file: UploadFile = File(...)):

    task, file = get_load_tasks(file)

    try:
        file_content = await file.read()

        data = {"data": file_content}

        result = app.send_task(
            task,
            kwargs=data,
        )

        return result.get()
    finally:

        await file.close()
