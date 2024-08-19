from pydantic import BaseModel, field_validator
from fastapi import UploadFile, HTTPException


class ModelSchema(BaseModel):
    model_name: str
    flavor: str
    model: UploadFile

    @field_validator("model", mode="before")
    @classmethod
    def validator_model(cls, model):
        if not model.filename.endswith(".pkl"):
            raise HTTPException(
                status_code=400, detail="Invalid file type. Please upload a .pkl file."
            )
        return model
