#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.

If the subreddit is valid, it fetches and prints the top 10 hot posts.
If the subreddit is invalid, it prints None.
"""
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: If the subreddit doesn't exist or there's an error.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        # Extract and print the titles of the first 10 hot posts
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    else:
        # If subreddit is invalid or does not exist, print None
        print(None)
