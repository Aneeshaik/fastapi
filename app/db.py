import aiosql
import asyncpg
from pathlib import Path

QUERIES_DIR = Path(__file__).parent / "queries"
queries = aiosql.from_path(QUERIES_DIR, "asyncpg")

_pool: asyncpg.Pool | None = None

async def init_pool(dsn: str):
    global _pool
    _pool = await asyncpg.create_pool(dsn)

async def close_pool():
    if _pool:
        await _pool.close()

async def get_db_conn():
    async with _pool.acquire() as conn:
        yield conn
