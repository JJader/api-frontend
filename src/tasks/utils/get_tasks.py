from typing import Tuple, Any
from fastapi import UploadFile
from schemas import ModelSchema, PredictSchema, ResultSchema
from celery.result import AsyncResult


def get_predict_tasks(request: dict) -> Tuple[str, Any]:
    task_name = "app.mlflow.tasks.predict"
    payload = PredictSchema.model_validate(request)
    data = payload.model_dump()

    return (task_name, data)


def get_load_result(request: AsyncResult) -> Tuple[str, Any]:
    task_name = request.name
    result = ResultSchema(
        task_id=request.task_id, result=request.result, status=request.status
    )

    data = result.model_dump()
    return (task_name, data)


async def get_load_tasks(
    model_name: str, flavor: str, request: UploadFile
) -> Tuple[str, Any]:
    task_name = "app.mlflow.tasks.load"

    model = ModelSchema(model_name=model_name, flavor=flavor, model=request)

    try:
        file_content = await model.model.read()

        data = {
            "data": file_content,
            "model_name": model.model_name,
            "backend": model.flavor,
        }

        return (task_name, data)

    finally:

        await model.model.close()
