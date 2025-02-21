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
    """
    headers = {'User-Agent': 'python:reddit.api.client:v1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  
        if response.status_code == 404:
            print("None")
            return
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            if data:
                for post in data:
                    print(post.get('data', {}).get('title'))
            else:
                print("None")
        else:
            print("None")            
    except Exception:
        print("None")
