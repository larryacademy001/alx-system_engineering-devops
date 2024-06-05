#!/usr/bin/python3
'''
This module contains function top_ten.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
    Prints the titles of the top ten hot posts for a given subreddit.
    '''
    user = {'User-Agent': 'larryacademy001'}
    apiURL = requests.get(
        'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit),
        headers=user
    ).json()
    try:
        for post in apiURL.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
