#!/usr/bin/python3
import requests
"""
Gets the number of subscribers of a subreddit.
"""


def number_of_subscribers(subreddit):
    """num of subs"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
