#!/usr/bin/python3
"""subreddit subscribers"""
import requests
import json

def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        r = requests.get(url, allow_redirects=False)
        if r.status_code == 200:
            dt = r.json()
            if 'data' in dt.keys():
                if 'subscribers' in dt['data'].keys():
                    return dt['data']['subscribers']
        return 0
    except requests.RequestException:
        return 0
