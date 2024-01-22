from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import database
from api_calls.routes import api_router
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(api_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Lógica antes de que la app comience
    await database.connect()
    yield
    # Lógica cuando la app se está cerrando
    await database.disconnect()


