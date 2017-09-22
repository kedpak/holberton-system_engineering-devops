#!/usr/bin/python3
"""
Print the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests

headers = {
    "User-Agent": "kpak"
}


def top_ten(subreddit):
    """
    return top ten hot lists
    """
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers=headers)
    if not r.ok:
        print ("None")
        return
    content = r.json()
    if content is None:
        print ("None")
        return
    if content["data"] is None:
        print ("None")
        return
    content = content.get('data', {}).get('children', {})
    if content is None:
        print ("None")
        return
    i = 0
    for data in content:
        if data is None:
            print ("None")
            return
        title = (data.get('data', {}).get('title'))
        if title is None:
            return
        print(title)
        i += 1
        if i == 10:
            break
    if i == 0:
        print ("None")
