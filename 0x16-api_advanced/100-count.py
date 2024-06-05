#!/usr/bin/python3
"""Module for a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
"""


import requests


def count_words(subreddit, word_list, after='', dict_word={}):
    """
    Queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces).
    Javascript should count as javascript, but java should not.
    If no posts match or the subreddit is invalid, it prints nothing.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of words to count.
        after (str): The parameter for pagination.
        dict_word (dict): Dictionary to store the count of words.
    """

    if not dict_word:
        for words in word_list:
            if words.lower() not in dict_word:
                dict_word[words.lower()] = 0

    if after is None:
        wordict = sorted(dict_word.items(), key=lambda x: (-x[1], x[0]))
        for words in wordict:
            if words[1]:
                print('{}: {}'.format(words[0], words[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'larryacademy001'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_art = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot_art:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in dict_word.keys():
                dict_word[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, dict_word)
