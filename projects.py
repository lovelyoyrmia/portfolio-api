from fastapi import APIRouter, Path
from pydantic import BaseModel
import json


project = APIRouter()

with open("portfolio.json", "r") as f:
    project_list = json.load(f)["projects"]


class Projects(BaseModel):
    id: int
    project_name: str
    category: str
    image_path: str
    image_list: list
    description: str
    date: int
    tools: str
    link_web: str


@project.get("/")
async def get_projects():
    return {"projects": project_list}
