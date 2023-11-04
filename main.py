import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database.databaseConnection import db_helper
from database.models import Base, Airport
from sqlalchemy import select
from sqlalchemy.engine import Result


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/airports")
async def get_airports():
    async with db_helper.engine.begin() as conn:
        query = select(Airport)
        result: Result = await conn.execute(query)
        data = result.mappings().all()
    return data


@app.get("/root")
def get_root():
    return {"message": "this is root"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
