from fastapi import APIRouter, Path
from pydantic import BaseModel
import json


route = APIRouter()

with open("portfolio.json", "r") as f:
    certif_list = json.load(f)["certificates"]


class Certificate(BaseModel):
    id: int
    name: str
    description: str
    image: str
    issued_date: int


@route.get("/")
async def get_certificate():
    return {"certificates": certif_list}
