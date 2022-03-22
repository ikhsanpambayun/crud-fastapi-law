from typing import Optional
from pydantic import BaseModel


class Guitar(BaseModel):
    id: int
    name: str
    type: str
    description: Optional[str] = None

    class Config:
        orm_mode = True