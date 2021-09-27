#!/usr/bin/python3
"""0. How many subs? - Module"""


def number_of_subscribers(subreddit):
    """ number_of_subscribers - retrieve aa number of subscribers"""
    import requests

    with requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit)
    ) as response:
        if response.status_code > 299:
            return 0
    n_subscribers = response.json()
    return n_subscribers.get("data").get("subscribers")
