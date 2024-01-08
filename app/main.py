from fastapi import FastAPI
from app.api import api_router

app = FastAPI(trace_configs=True)

app.include_router(api_router)
