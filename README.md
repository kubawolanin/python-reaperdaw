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


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
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
