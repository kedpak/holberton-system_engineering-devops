#!/usr/bin/python3
"""
ueries the Reddit API (https://www.reddit.com/dev/api/)
and returns the number of subscribers. I invalid subreddit
return 0.
"""
import requests
import sys

headers = {
    "User-Agent": "kpak"
}


def number_of_subscribers(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers=headers)
    if not r.ok:
        return 0
    content = r.json()
    return content["data"]["subscribers"]
