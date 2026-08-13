from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from app.db import init_pool, close_pool, get_db_conn, queries
from app.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_pool(settings.database_url)
    yield
    await close_pool()

app = FastAPI(title="Payments API", lifespan=lifespan)

@app.get('/health')
async def health():
    return {"status": "ok"}

