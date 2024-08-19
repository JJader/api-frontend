# teste.py

from fastapi import APIRouter, UploadFile, File
from tasks import app, get_load_tasks

router = APIRouter()


@router.post("/model/load")
async def read_load(model_name: str, flavor: str, file: UploadFile = File(...)):

    task, data = await get_load_tasks(model_name, flavor, file)

    result = app.send_task(
        task,
        kwargs=data,
    )

    return result.get()
