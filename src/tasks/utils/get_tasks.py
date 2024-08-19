from typing import Tuple, Any
from schemas import PredictSchema


def get_predict_tasks(request: dict) -> Tuple[str, Any]:
    task_id = "app.mlflow.tasks.predict"
    payload = PredictSchema.model_validate(request)

    return (task_id, payload.data)
