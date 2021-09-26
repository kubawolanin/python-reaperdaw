import aiohttp
import asyncio
from reaperdaw import Reaper


async def main(host="localhost", port="8080", username="", password=""):

    async with aiohttp.ClientSession() as session:
        reaper = Reaper(session, host, port, username, password)
        status = await reaper.getStatus()
        print("Status:", status)
        await reaper.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main(port="9999"))
