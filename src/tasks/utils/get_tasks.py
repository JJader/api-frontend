from typing import Tuple, Any
from schemas import PredictSchema
from fastapi import UploadFile, HTTPException


def get_predict_tasks(request: dict) -> Tuple[str, Any]:
    task_id = "app.mlflow.tasks.predict"
    payload = PredictSchema.model_validate(request)

    return (task_id, payload.data)


def get_load_tasks(request: UploadFile) -> Tuple[str, Any]:
    task_id = "app.mlflow.tasks.load"
    if not request.filename.endswith(".pkl"):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Please upload a .pkl file."
        )

    return (task_id, request)
