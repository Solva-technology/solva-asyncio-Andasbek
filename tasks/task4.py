import asyncio
from typing import Union


async def safe_divide(a: float, b: float) -> Union[float, str]:
    """Асинхронное деление с обработкой деления на ноль."""
    await asyncio.sleep(0.1)
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


async def run_divisions() -> list[Union[float, str]]:
    """Запускает деление для набора пар чисел."""
    pairs = [(10, 2), (5, 0), (8, 4)]
    tasks = [safe_divide(a, b) for a, b in pairs]
    return await asyncio.gather(*tasks)
