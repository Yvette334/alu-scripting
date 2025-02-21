#!/usr/bin/python3
"""
This module queries the Reddit API and prints the top 10 hot posts for a given subreddit.
"""

import requests
import sys
import io
import sys
from requests.auth import HTTPBasicAuth

# Ensure that the output uses UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Reddit API credentials (replace these with your actual credentials)
    client_id = "YOUR_CLIENT_ID"        # Replace with your client ID
    client_secret = "YOUR_CLIENT_SECRET" # Replace with your client secret

    headers = {
        'User-Agent': 'ALX-API-Checker/1.0 (by YourRedditUsername)',  # Custom User-Agent
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'application/json'
    }

    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.get(url, headers=headers, auth=auth)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("No posts found.")
        else:
            for post in posts:
                title = post['data'].get('title')
                
                # Try to print title, handle any encoding issues
                try:
                    print(title)
                except UnicodeEncodeError:
                    print(title.encode('utf-8'))
    else:
        print("None")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

