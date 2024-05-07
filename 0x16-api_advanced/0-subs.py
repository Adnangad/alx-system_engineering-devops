#!/usr/bin/python3
"""
Gets the number of subscribers from a subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers of a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    ag = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=ag)
    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0
