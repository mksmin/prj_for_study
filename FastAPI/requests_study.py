import requests
import pprint

import aiohttp
import asyncio


response = requests.get('http://api.github.com')
response_json = response.request.headers
pprint.pprint(response_json)

User_agent = {'User-Agent': 'maxLive'}
response = requests.get('http://api.github.com', headers=User_agent)

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())