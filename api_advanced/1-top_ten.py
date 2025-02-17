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
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    sort = 'top'
    limit = 10

    # Make the GET request to Reddit's API
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False  # Prevent following redirects
    )
    
    # Check for a successful response (status code 200)
    if res.status_code == 200:
        try:
            # Retrieve and print the top 10 posts from the response
            for post in res.json()['data']['children'][0:10]:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
