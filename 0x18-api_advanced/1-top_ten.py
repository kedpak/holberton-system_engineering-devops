#!/usr/bin/python3
"""
Print the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests
import sys
import json
headers = {
    "User-Agent": "kpak"
}


def top_ten(subreddit):
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers=headers)
    if not r.ok:
        print (None)
    content = r.json()
    i = 0
    for data in content["data"]["children"]:
        print(json.dumps(data["data"]["title"], indent=4))
        i += 1
        if i == 10:
            break
