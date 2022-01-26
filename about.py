from fastapi import APIRouter, Path
from pydantic import BaseModel
import json


about = APIRouter()

with open("portfolio.json", "r") as f:
    about_list = json.load(f)["about"]


@about.get("/")
async def get_about():
    return {"about": about_list}


@about.get("/skills")
async def get_skills():
    return {"skills": about_list["skills"]}


@about.get("/experience")
async def get_experience():
    return {"experience": about_list["experience"]}


@about.get("/education")
async def get_education():
    return {"education": about_list["education"]}
