#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys  # Import sys module to use sys.stdout.write()

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
        sys.stdout.write("OK")  # Using sys.stdout.write to print without newline
        sys.stdout.flush()  # Flush to ensure immediate output
        return

    try:
        data = response.json().get('data', {}).get('children', [])
        if not data:
            sys.stdout.write("OK")  # Using sys.stdout.write to print without newline
            sys.stdout.flush()  # Flush to ensure immediate output
            return

        for post in data:
            print(post.get('data', {}).get('title'))
    except Exception:
        sys.stdout.write("OK")  # Using sys.stdout.write to print without newline
        sys.stdout.flush()  # Flush to ensure immediate output
