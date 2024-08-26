# teste.py

from fastapi import APIRouter
from tasks import app, get_predict_tasks
from schemas import PredictSchema

router = APIRouter()


@router.post("/model/predict")
async def read_predict(payload: PredictSchema):
    task, data = get_predict_tasks(payload)

    predict_task = app.send_task(
        task,
        kwargs=data,
    )

    result = {"result": predict_task.get()}

    return result
