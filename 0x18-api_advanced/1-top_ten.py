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
        return
    content = r.json()
    print(json.dumps(content, indent=4))
    i = 0
    for data in content["data"]["children"]:
        if data["data"]["title"] is None:
            return
        print(data["data"]["title"])
        i += 1
        if i == 10:
            break
    if i == 0:
        print (None)
