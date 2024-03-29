from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from certificates import route
from projects import project
from about import about
from services import services

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lovelyoyrmia.github.io", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route, prefix="/certificates", tags=["certificates"])
app.include_router(project, prefix="/projects", tags=["projects"])
app.include_router(about, prefix='/about', tags=['about'])
app.include_router(services, prefix='/services', tags=['services'])

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, workers=4)
