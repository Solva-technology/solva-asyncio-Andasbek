import asyncio
import pytest

async def safe_divide(a, b):
    await asyncio.sleep(0.1)
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"

async def run_divisions():
    pairs = [(10, 2), (5, 0), (8, 4)]
    tasks = [safe_divide(a, b) for a, b in pairs]
    return await asyncio.gather(*tasks)
