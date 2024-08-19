from typing import Tuple, Any
from schemas import PredictSchema
from fastapi import UploadFile
from schemas import ModelSchema


def get_predict_tasks(request: dict) -> Tuple[str, Any]:
    task_id = "app.mlflow.tasks.predict"
    payload = PredictSchema.model_validate(request)

    return (task_id, payload.data)


async def get_load_tasks(
    model_name: str, flavor: str, request: UploadFile
) -> Tuple[str, Any]:
    task_id = "app.mlflow.tasks.load"

    model = ModelSchema(model_name=model_name, flavor=flavor, model=request)

    try:
        file_content = await model.model.read()

        data = {
            "data": file_content,
            "model_name": model.model_name,
            "backend": model.flavor,
        }

        return (task_id, data)

    finally:

        await model.model.close()
