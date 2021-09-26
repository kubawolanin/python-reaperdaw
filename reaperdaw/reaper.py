"""Asynchronous Python client for Reaper DAW"""
import aiohttp
import logging
import json

from .exceptions import ReaperError
from .models import parse

# logging.basicConfig(filename="test.log", level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

RESPONSE_STATUS = "status"
RESPONSE_STATUSTEXT = "statustext"
RESPONSE_ERRORSTATUS = "Error"


class Reaper:
    def __init__(self, session, host="localhost", port="8080", username="", password=""):
        self._rh = _RequestsHandler(session, host, port, username, password)
        self._status = None

    async def sendCommand(self, command):
        data = await self._rh.get(command=command)
        if RESPONSE_STATUS in data and data[RESPONSE_STATUS] == RESPONSE_ERRORSTATUS:
            raise ReaperError(RESPONSE_ERRORSTATUS, data[RESPONSE_STATUSTEXT])
        return data

    async def getStatus(self):
        result = await self.sendCommand("NTRACK;TRANSPORT;BEATPOS;GET/40364;GET/1157;TRACK;")
        self._status = result
        status = parse(result)
        return json.dumps(status)

    @property
    def status(self):
        return self._status

    async def rewind(self):
        await self.sendCommand("40084")

    async def stop(self):
        await self.sendCommand("1016")

    async def play(self):
        await self.sendCommand("1007")

    async def pause(self):
        await self.sendCommand("1008")

    async def fastForward(self):
        await self.sendCommand("40085")

    async def record(self):
        await self.sendCommand("1013")

    async def toggleRepeat(self):
        await self.sendCommand("1068")

    async def toggleMetronome(self):
        await self.sendCommand("40364")

    async def enableMetronome(self):
        await self.sendCommand("41745")

    async def disableMetronome(self):
        await self.sendCommand("41746")

    async def toggleMuteMasterTrack(self):
        await self.sendCommand("14")

    async def saveProject(self):
        await self.sendCommand("40026")

    async def saveAllProjects(self):
        await self.sendCommand("40897")

    async def setMasterVolume(self, volume):
        await self.sendCommand(f"SET/TRACK/0/VOL/{volume}")


class _RequestsHandler:
    """Internal class to create Reaper requests"""

    def __init__(self, session: aiohttp.ClientSession, host, port, username, password):
        self.headers = {"Accept": "text/plain"}

        self.session = session
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    async def get(self, command):
        url = f"http://{self.username}:{self.password}@{self.host}:{self.port}/_/{command}"

        _LOGGER.debug("Sending request to: %s", url)
        async with self.session.get(
            url, headers=self.headers
        ) as response:
            if response.status != 200:
                _LOGGER.warning(
                    "Invalid response from Reaper API: %s", response.status
                )
                raise ReaperError(response.status, await response.text())

            data = await response.text()
            _LOGGER.debug(data)
            return data
