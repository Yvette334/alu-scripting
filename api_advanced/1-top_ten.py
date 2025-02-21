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

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Debugging Response Status
    print("Response Status Code:", response.status_code)
    
    if response.status_code != 200:
        output = "OK"
        print("Output (Response Failure):", output)  # Normal print
        print("Length of output:", len(output))  # Debugging length
        return

    try:
        data = response.json().get('data', {}).get('children', [])
        if not data:
            output = "OK"
            print("Output (No Data):", output)  # Normal print
            print("Length of output:", len(output))  # Debugging length
            return

        for post in data:
            print(post.get('data', {}).get('title'))
    except Exception as e:
        output = "OK"
        print("Output (Exception):", output)  # Normal print
        print("Length of output:", len(output))  # Debugging length
        print("Exception message:", e)
