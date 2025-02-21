#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit: The subreddit to query

    Returns:
        None if subreddit is invalid
    """
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:reddit.api.client:v1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit exists (status code 200)
        if response.status_code != 200:
            print(None)
            return

        # Parse JSON response
        data = response.json().get('data', {}).get('children', [])
        
        # Print titles of first 10 hot posts
        for post in data:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
