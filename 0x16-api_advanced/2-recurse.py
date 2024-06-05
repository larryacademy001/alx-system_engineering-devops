#!/usr/bin/python3
"""
Contains the recurse function to fetch all hot post titles
from a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively fetches titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot posts.
        after (str): The parameter for pagination.
        count (int): The count of posts fetched so far.

    Returns:
        list: A list of titles of all hot posts on the subreddit,
        or None if subreddit is invalid.
    """
    apiURL = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/larryacademy001)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(apiURL, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
