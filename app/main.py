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

@app.post("/create_payment")
async def create_payment(amount: float, currency: str, db=Depends(get_db_conn)):
    payment_id = queries.create_payment(db, amount=amount, currency=currency, status="pending")
    return {"id": payment_id}

@app.get("/list_payments")
async def list_payments(db=Depends(get_db_conn)):
    payments = queries.list_payments(db)
    return {"payments": payments}

@app.get("/payments/{payment_id}")
async def get_payment(payment_id: int, db=Depends(get_db_conn)):
    return await queries.get_payment_by_id(db, payment_id=payment_id)