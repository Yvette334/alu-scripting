#!/usr/bin/python3
'''A module containing a function that queries the Reddit API and prints the titles of the first 10 "top" posts
listed for a given subreddit. If the subreddit does not exist, it prints None.
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
    time_filter = 'all'  # Specify the time period for 'top' posts (can be 'all', 'day', 'week', etc.)
    limit = 10
    
    res = requests.get(
        f'{BASE_URL}/r/{subreddit}/.json?sort={sort}&t={time_filter}&limit={limit}',
        headers=api_headers,
        allow_redirects=False
    )
    
    if res.status_code == 200:
        try:
            for post in res.json()['data']['children']:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)

