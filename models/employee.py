from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"


class Employee(BaseModel):
    id:Optional[int]
    name:Optional[str] = None
    surname:Optional[str] = None