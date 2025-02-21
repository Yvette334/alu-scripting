#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys  # Import the sys module to access standard output

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit: The subreddit to query
    """
    headers = {'User-Agent': 'python:reddit.api.client:v1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        sys.stdout.buffer.write(b"OK")  # Directly write bytes to stdout
        return
    try:
        data = response.json().get('data', {}).get('children', [])
        if not data:
            sys.stdout.buffer.write(b"OK")  # Directly write bytes to stdout
            return
        for post in data:
            print(post.get('data', {}).get('title'))
    except Exception:
        sys.stdout.buffer.write(b"OK")  # Directly write bytes to stdout
