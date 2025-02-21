#!/usr/bin/python3
"""
This module queries the Reddit API and prints the top 10 hot posts for a given subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'ALX-API-Checker/1.0 (by YourRedditUsername)'  # Use a custom User-Agent
    }

    response = requests.get(url, headers=headers, allow_redirects=True)

    # Debugging print statements
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("No posts found.")
        else:
            for post in posts:
                print(post['data'].get('title'))
    else:
        print("None")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
