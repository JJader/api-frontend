from pydantic import BaseModel


class PredictSchema(BaseModel):
    model_name: str
    data: dict
