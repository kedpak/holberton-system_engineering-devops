#!/usr/bin/python3
"""
Print the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests
import sys

headers = {
    "User-Agent": "kpak"
}


def recurse(subreddit, hot_list=[], after=None):
    """ print all hot topics in subreddit"""
    if len(hot_list) == 0:
        url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "http://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    r = requests.get(url, headers=headers)
    if not r.ok:
        return None
    content = r.json()
    hot_post = content["data"]["children"]
    if hot_post is None:
        return None
    for i in range(len(content["data"]["children"])):
        hot_list.append(content["data"]["children"][i]["data"]["title"])
    if content["data"]["after"] is not None:
        recurse(subreddit, hot_list, content["data"]["after"])
    return hot_list
