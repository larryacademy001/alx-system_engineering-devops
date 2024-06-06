#!/usr/bin/python3
"""
Script that queries the number of subscribers on a given
Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total subscriber count for the specified subreddit."""
    apiURL = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "larryacademy001"}
    response = requests.get(apiURL, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
