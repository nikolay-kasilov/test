from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
class Item(BaseModel):
     full_name: str
     age: int
     bio : str



