#!/usr/bin/python3
"""A module containing functions for working with the Reddit API."""

import requests
import sys

BASE_URL = 'https://www.reddit.com'
"""Reddit's base API URL."""

def top_ten(subreddit):
    """Retrieves the title of the top ten posts from a given subreddit."""
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    res = requests.get(
        f'{BASE_URL}/r/{subreddit}/hot.json?limit=10',
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        hot_posts = res.json().get("data", {}).get("children", [])
        if hot_posts:
            for post in hot_posts[:10]:
                print(post.get("data", {}).get("title", None))
        else:
            print(None)
    else:
        print(None)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

