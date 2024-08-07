from datetime import datetime

from pydantic import BaseModel


class MySchema(BaseModel):
    id: int = None
    name: str = None
    age: int = None
    created_at: datetime = None
    updated_at: datetime = None
