#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''

import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a given subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    
    # Construct the URL to access the subreddit
    url = f'{BASE_URL}/r/{subreddit}/.json?sort=top&limit=10'
    
    # Send the GET request
    res = requests.get(url, headers=api_headers, allow_redirects=False)
    
    # Check if we have a valid response (status code 200)
    if res.status_code == 200:
        try:
            # Parse the JSON response and retrieve the top 10 posts
            posts = res.json().get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
