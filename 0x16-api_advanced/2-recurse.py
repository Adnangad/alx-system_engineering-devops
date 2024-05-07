#!/usr/bin/python3
"""
Gets the list of titles of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns the list of all hot articles"""
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'after':after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')
        if children:
            for child in children:
                title = child.get('data').get('title')
                hot_list.append(title)
            after = data['data']['after']
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
