import asyncio


async def fast_task() -> str:
    await asyncio.sleep(0.1)
    return "fast"


async def medium_task() -> str:
    await asyncio.sleep(0.3)
    return "medium"


async def slow_task() -> str:
    await asyncio.sleep(1.0)
    return "slow"


async def first_complete() -> str:
    tasks = [
        asyncio.create_task(fast_task()),
        asyncio.create_task(medium_task()),
        asyncio.create_task(slow_task()),
    ]

    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )

    # Одна завершённая задача гарантирована
    first_task = next(iter(done))
    first_result = first_task.result()

    # Отменяем и корректно дожидаемся остальных
    for task in pending:
        task.cancel()
    await asyncio.gather(*pending, return_exceptions=True)

    return first_result


if __name__ == "__main__":
    print(asyncio.run(first_complete()))
