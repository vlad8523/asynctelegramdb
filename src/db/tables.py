from .base import BaseModel

from sqlalchemy.ext.asyncio import AsyncEngine


async def refresh_table(engine: AsyncEngine):
    async with engine.begin() as conn:
        print(BaseModel.metadata)
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
