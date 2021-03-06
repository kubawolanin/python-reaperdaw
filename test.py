import aiohttp
import asyncio
import json
from reaperdaw import Reaper


async def main(host="localhost", port="9999", username="", password=""):

    async with aiohttp.ClientSession() as session:
        reaper = Reaper(session, host, port, username, password)
        await reaper.setMasterVolume(1)

        status = await reaper.getStatus()
        response = json.loads(status)
        print("Status:", status)
        print("Number of tracks:", response["number_of_tracks"])
        print("Number of armed tracks:", response["number_of_armed_tracks"])
        print("Armed tracks:", response["armed_tracks"])
        print("Play state:", response["play_state"])
        print("Time signature:", response["time_signature"])


loop = asyncio.get_event_loop()
loop.run_until_complete(main(port="9999"))
