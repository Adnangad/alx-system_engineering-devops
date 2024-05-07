#!/usr/bin/python3
import requests
"""
Gets the number of subscribers of a subreddit.
"""


def number_of_subscribers(subreddit):
    """num of subs"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 {by /u/bdov_}'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    return data['data']['subscribers']
