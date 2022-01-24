from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from certificates import route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route, prefix="/certificates", tags=["certificates"])

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
