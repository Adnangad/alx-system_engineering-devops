#!/usr/bin/python3
"""
Gets the top ten titles of a subreddit.
"""
import requests


def top_ten(subreddit):
    """num of subs"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    try:
        rez = data.get('data').get('children')
        for post in rez:
            title = post.get('data').get('title')
            print(title)
    except Exception:
        print("None")
