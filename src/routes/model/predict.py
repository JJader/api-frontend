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

    predict = predict_task.get()

    result = {"result": predict.get("result"), "metadata": predict.get("model")}

    return result
