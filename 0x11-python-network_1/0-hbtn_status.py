#!/usr/bin/python3
"""This script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:"
          "\n\t- type: {}"
          "\n\t- content: {}"
          "\n\t- utf8 content: {}".format(
                type(html), html, html.decode("utf-8")))
