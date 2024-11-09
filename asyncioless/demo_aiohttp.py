import asyncio
import aiohttp
from dataclasses import dataclass
from loguru import logger


async def demo_query_httpbin():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as response:
            print(response.status)
            print(await response.text())
            print(await response.json())


@dataclass(frozen=True)
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name='ipify', url='https://api.ipify.org/?format=json', field='ip'),
    Service(name='ip-api', url='http://ip-api.com/json', field='query'),
]


async def fetch_json(utl: str, session: aiohttp.ClientSession) -> dict:
    async with session.get(utl) as response:
        data: dict = await response.json()
        logger.info("result {} for {}", data, response.url)
        return data


async def fetch_ip(service: Service) -> str | None:
    logger.info('fetch ip from service {}', service.name)

    async with aiohttp.ClientSession() as session:
        data = await fetch_json(service.url, session)
        return data.get(service.field)


async def get_my_ip(timeout: int | float = 0.5):
    logger.info('Search for ip')
    tasks = {
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }
    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:  # type: asyncio.Task
        task.cancel()
        logger.info('Cancel task for {}', task)

    my_ip = ''
    for task in done:  # type: asyncio.Task
        my_ip = task.result()
        break
    else:
        logger.info('Could not fetch ip')
    return my_ip


def main():
    # asyncio.run(demo_query_httpbin())
    ip = asyncio.run(get_my_ip(0.1))
    logger.info('result ip: {}', ip)


if __name__ == '__main__':
    main()
