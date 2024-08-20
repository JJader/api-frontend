# teste.py

from fastapi import APIRouter, UploadFile, File
from tasks import app, get_load_tasks, get_load_result

router = APIRouter()


@router.post("/model/load")
async def read_load(model_name: str, flavor: str, file: UploadFile = File(...)):

    task, data = await get_load_tasks(model_name, flavor, file)

    result = app.send_task(
        task,
        kwargs=data,
    )

    return {"task_id": result.id}


@router.get("/model/loads")
async def read_task_load(task_id: str):

    result = app.AsyncResult(task_id)
    task_id, metadados = get_load_result(result)
    # {"status": result.status, "task_id": result.id, "result": result.result}

    return metadados
