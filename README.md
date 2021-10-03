# python-reaperdaw

[![GitHub Release][releases-shield]][releases]
[![PyPI][pypi-releases-shield]][pypi-releases]
[![PyPI - Downloads][pypi-downloads]][pypi-statistics]
[![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]
[![PayPal_Me][paypal-me-shield]][paypal-me]

Python wrapper for REAPER DAW REST interface.

Please refer to ReaTeam's [web interface modding](https://github.com/ReaTeam/Doc/blob/master/web_interface_modding.md) documentation for API insights.

## Setup in Reaper

1. Launch your Reaper DAW
1. Hit `Ctrl + P` or go to Options > Preferences
1. Navigate to "Control/OSC/web" menu and click "Add"
1. From the "Control surface mode" dropdown menu choose "Web browser interface"
1. Set the web interface port or leave default `8080`
1. Optionally set username:password
1. Optionally set the default web interface
1. Copy the Access URL and paste it in your browser - now your Reaper has a web interface.
1. Hit OK in both preference windows

## Example usage

```python
import aiohttp
import asyncio
import json
from reaperdaw import Reaper


async def main(host="localhost", port="8080", username="", password=""):

    async with aiohttp.ClientSession() as session:
        reaper = Reaper(session, host, port, username, password)

        # Sets Master Volume to 0db (maximum volume)
        await reaper.setMasterVolume(1)

        status = await reaper.getStatus()
        response = json.loads(status)
        print("Status:", status)
        print("Number of tracks:", response["number_of_tracks"])
        print("Time signature:", response["time_signature"])
        print("Play state:", response["play_state"])
        print("Repeat:", response["repeat"])
        print("Metronome:", response["metronome"])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### getStatus response

```json
{
  "tracks": [
    {
      "index": 0,
      "name": "MASTER",
      "flags": [],
      "volume": "1.000000",
      "pan": "0.000000",
      "last_meter_peak": "-1500",
      "last_meter_pos": "-1500",
      "width_pan2": "1.000000",
      "panmode": "0",
      "sendcnt": "0",
      "recvcnt": "0",
      "hwoutcnt": "1",
      "color": "#000000"
    },
    {
      "index": 1,
      "name": "Track 1",
      "flags": [],
      "volume": "1.000000",
      "pan": "0.000000",
      "last_meter_peak": "-1500",
      "last_meter_pos": "-1500",
      "width_pan2": "1.000000",
      "panmode": "3",
      "sendcnt": "0",
      "recvcnt": "0",
      "hwoutcnt": "0",
      "color": "#764e78"
    },
    {
      "index": 2,
      "name": "Track 2",
      "flags": ["selected"],
      "volume": "1.000000",
      "pan": "0.000000",
      "last_meter_peak": "-1500",
      "last_meter_pos": "-1500",
      "width_pan2": "1.000000",
      "panmode": "3",
      "sendcnt": "0",
      "recvcnt": "0",
      "hwoutcnt": "0",
      "color": "#d9c25b"
    }
  ],
  "repeat": true,
  "metronome": false,
  "time_signature": "4/4",
  "beatpos": {
    "position_seconds": "0.000000000000000",
    "full_beat_position": "0.000000000000000",
    "measure_cnt": "0",
    "beats_in_measure": "0.000000000010000"
  },
  "play_state": "stopped",
  "transport": {
    "playstate": "stopped",
    "position_seconds": "0.000000",
    "repeat": true,
    "position_string": "1.1.00",
    "position_string_beats": "1.1.00"
  },
  "number_of_tracks": 2
}
```

[releases]: https://github.com/kubawolanin/python-reaperdaw/releases
[releases-shield]: https://img.shields.io/github/release/kubawolanin/python-reaperdaw.svg?style=popout
[pypi-releases]: https://pypi.org/project/python-reaperdaw/
[pypi-statistics]: https://pepy.tech/project/python-reaperdaw
[pypi-releases-shield]: https://img.shields.io/pypi/v/python-reaperdaw
[pypi-downloads]: https://pepy.tech/badge/python-reaperdaw/month
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/kubawolanin
[paypal-me-shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal-me]: https://www.paypal.me/kubawolanin
