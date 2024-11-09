import asyncio
from loguru import logger


async def foo():
    logger.info('Start async foo')
    await asyncio.sleep(4)
    logger.info('Finish async foo')


async def bar():
    logger.info('Start async bar')
    await asyncio.sleep(1)
    logger.info('Finish async bar')


async def run_by_one():
    # await foo()
    # await bar()
    coro_foo = foo()
    coro_bar = bar()
    await coro_foo
    await coro_bar


def generate_sleep_time(task_id: int):
    to_sleep = 1

    if task_id % 5 == 0:
        is_add = (task_id // 10) % 2 == 0
        to_sleep += (task_id / 1000) * (1 if is_add else -1)

    return to_sleep


async def some_func(task_id: int):
    to_sleep = generate_sleep_time(task_id)
    logger.info('Start task #{:4d} and sleep {:.2f}', task_id, to_sleep)
    await asyncio.sleep(to_sleep)
    logger.info('Finish task #{:4d}', task_id)


async def run_many():
    # await some_func(1)
    # await some_func(123)

    # task = asyncio.create_task(some_func(432))
    tasks = {
        asyncio.create_task(
            some_func(task_id)
        )
        for task_id in range(1, 125)
    }
    coro = asyncio.wait(tasks)

    await coro


async def main():
    logger.info('Start async main')
    # await gather(foo(), bar())
    await run_many()
    logger.warning('finished async main')


if __name__ == '__main__':
    asyncio.run(main())
