import json
from aiohttp import ClientSession
from asyncio import events

async def call_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json(encoding='utf-8')

            return data

def do_call_api(url: str):
    loop = events.get_event_loop()
    return loop.run_until_complete(call_api(url))
