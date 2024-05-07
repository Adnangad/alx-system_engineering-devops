#!/usr/bin/python3
import requests
"""
Gets the number of subscribers of a subreddit.
"""


def top_ten(subreddit):
    """num of subs"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        print("None")
