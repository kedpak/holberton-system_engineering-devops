#!/usr/bin/python3
"""1. Top Ten"""
import requests


def top_ten(subreddit):
    """return titles of the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    r = requests.get(url, headers={'User-agent': 'Hunter'})
    if not r.ok:
        # invalid subreddit
        print("None")
        return

    r_json = r.json()
    if r_json is None:
        print("None")
        return

    posts = r_json.get('data', {}).get('children', {})
    if posts is None:
        print("None")
        return

    count = 0
    for post in posts:
        title = (post.get('data', {}).get('title'))
        if title is None:
            return

        # print title of hot post
        print("{}".format(title))

        if count == 9:
            break
        count += 1

    if count == 0:
        print("None")
        return

if __name__ == "__main__":
    top_ten(subreddit)
