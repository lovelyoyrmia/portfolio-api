from fastapi import APIRouter, Path
from pydantic import BaseModel
import json


services = APIRouter()

with open("portfolio.json", "r") as f:
    services_list = json.load(f)["services"]

class Services(BaseModel):
    id: int
    title: str
    icon: str
    description: str

@services.get("/")
async def get_services():
    return {"services": services_list}
