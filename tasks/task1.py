import aiohttp
import asyncio
import pytest


async def fetch_status(session, url: str) -> int:
    async with session.get(url) as response:
        return response.status
    
async def fetch_all(urls: list) -> list:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        return await asyncio.gather(*tasks)


# Тесты
@pytest.mark.asyncio
async def test_fetch_status_200():
    async with aiohttp.ClientSession() as session:
        status = await fetch_status(session, 'https://httpbin.org/status/200')
        print("Полученный статус:", status)
        assert status == 200

@pytest.mark.asyncio
async def test_fetch_all():
    urls = [
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/404',
        'https://httpbin.org/status/500'
    ]
    statuses = await fetch_all(urls)
    assert statuses == [200, 404, 500]

if __name__ == "__main__":
    asyncio.run(test_fetch_status_200())
    asyncio.run(test_fetch_all())
    print("All tests passed.")
