#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) and uses
   the GitHub API to display your id
"""

import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    headers = {
                   "Accept": "application/vnd.github+json",
              }
    with requests.get(url, headers=headers) as response:
        for commit in response.json()[:10]:
            print("{}: {}".format(
                        commit.get('sha'),
                        commit.get('commit').get('author').get('name')))
