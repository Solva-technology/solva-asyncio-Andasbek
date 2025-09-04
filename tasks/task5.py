import asyncio


async def fast_task():
    await asyncio.sleep(0.1)
    return "fast"

async def medium_task():
    await asyncio.sleep(0.3)
    return "medium"

async def slow_task():
    await asyncio.sleep(1)
    return "slow"

async def first_complete():
    tasks = [
        asyncio.create_task(fast_task()),
        asyncio.create_task(medium_task()),
        asyncio.create_task(slow_task())
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first_result = None
    for task in done:
        first_result = await task
        break

    for task in pending:
        task.cancel()

    return first_result

if __name__ == "__main__":
    print(asyncio.run(first_complete()))