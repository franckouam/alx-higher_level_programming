#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays the
   body of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == '__main__':
    with requests.get(sys.argv[1]) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
