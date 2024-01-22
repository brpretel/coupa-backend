from fastapi import FastAPI
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


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

