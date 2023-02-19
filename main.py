from src.db import refresh_table


async def on_startup(dp):
    from loader import engine

    await refresh_table(engine)

    pass
    # async with engine.begin() as conn:
    #     # await engine
    #     await conn.run_sync(BaseModel.metadata.drop_all)
    #     await conn.run_sync(BaseModel.metadata.create_all)


if __name__ == '__main__':
    from aiogram import executor
    from src import dp

    executor.start_polling(dp, on_startup=on_startup)
