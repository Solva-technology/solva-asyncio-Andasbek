import asyncio
import pytest


async def limited_worker(task_id, semaphore):
    async with semaphore:
        await asyncio.sleep(0.1)
        return task_id

async def limited_runner():
    semaphore = asyncio.Semaphore(2)
    tasks = [limited_worker(i, semaphore) for i in range(5)]
    return await asyncio.gather(*tasks)

# Тесты
@pytest.mark.asyncio
async def test_limited_worker_returns_id():
    sem = asyncio.Semaphore(1)
    result = await limited_worker(42, sem)
    assert result == 42

@pytest.mark.asyncio
async def test_limited_runner_returns_all_ids():
    results = await limited_runner()
    assert sorted(results) == [0, 1, 2, 3, 4]
    assert results == [0, 1, 2, 3, 4]

if __name__ == "__main__":
    asyncio.run(test_limited_worker_returns_id())
    asyncio.run(test_limited_runner_returns_all_ids())
    print("All tests passed.")