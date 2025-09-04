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

# Тесты
@pytest.mark.asyncio
async def test_safe_divide():
    result1 = await safe_divide(10, 2)
    assert result1 == 5.0

    result2 = await safe_divide(5, 0)
    assert result2 == "Ошибка деления"

    result3 = await safe_divide(8, 4)
    assert result3 == 2.0

@pytest.mark.asyncio
async def test_run_divisions_expected_results():
    results = await run_divisions()
    assert results == [5.0, "Ошибка деления", 2.0]

if __name__ == "__main__":
    asyncio.run(test_safe_divide())
    asyncio.run(test_run_divisions_expected_results())
    print("All tests passed.")