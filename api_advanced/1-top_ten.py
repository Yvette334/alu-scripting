#!/usr/bin/python3
"""
Script that fetches the top 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        None: If the subreddit doesn't exist or there's an error.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}/hot.json"
    
    # Request without following redirects to avoid redirects to search results
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
    
    # Check if the status code is 200 (OK) to confirm subreddit exists
    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(json_data['data']['children'][i]['data']['title'])
    else:
        # Print None if subreddit does not exist
        print(None)
