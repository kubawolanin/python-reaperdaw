import aiohttp
import asyncio
import json
from reaperdaw import Reaper


async def main(host="localhost", port="8080", username="", password=""):

    async with aiohttp.ClientSession() as session:
        reaper = Reaper(session, host, port, username, password)
        await reaper.setMasterVolume(1)

        status = await reaper.getStatus()
        response = json.loads(status)
        print("Status:", status)
        print("Number of tracks:", response["number_of_tracks"])


loop = asyncio.get_event_loop()
loop.run_until_complete(main(port="9999"))
