from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"


class Employee(BaseModel):
    id:int
    name:str
    surname:Optional[str] = None