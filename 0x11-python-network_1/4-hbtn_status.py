#!/usr/bin/python3
"""This script that fetches https://alx-intranet.hbtn.io/status"""

import requests

res = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:\n\t"
      "- type: {}\n\t"
      "- content: {}".format(type(res.text), res.text))
