from pydantic import BaseModel
from typing import Union


class ResultSchema(BaseModel):
    status: str
    task_id: str
    result: Union[None, dict]
