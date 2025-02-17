#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data").get("children")
        if posts:
            for i in range(min(10, len(posts))):
                print(posts[i].get("data").get("title"))
        else:
            print(None)
    except ValueError:
        print(None)
