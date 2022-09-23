#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    with requests.post(url, data=data) as response:
        try:
            j = response.json()
            if j:
                for key, value in j.items():
                    print("[{}] {}".format(key, value))
            else:
                print('No result')
        except requests.exceptions.JSONDecodeError:
            print("Not a valid JSON")
