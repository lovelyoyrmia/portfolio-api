from fastapi import FastAPI
import uvicorn
from certificates import route

app = FastAPI()

app.include_router(route, prefix="/certificates", tags=["certificates"])

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
