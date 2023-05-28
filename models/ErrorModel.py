from typing import Optional

class ErrorModel:
    def __init__(self, message:str, statuscode: Optional[int] = 500):
        self.message:str = message
        self.statuscode:int = statuscode
