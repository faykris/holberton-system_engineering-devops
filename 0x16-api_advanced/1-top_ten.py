#!/usr/bin/python3
"""1. Top Ten- Module"""


def top_ten(subreddit):
    """top ten - prints the titles of the first 10 hot posts"""
    import requests

    response = requests.get(
            "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
            headers={"User-Agent": "Mozilla",
                     "Content-Type": "application/json"},
            allow_redirects=False,
    )
    if response.status_code > 299:
        print(None)
    else:
        top_10 = response.json()
        for ele in top_10.get("data").get("children"):
            print(ele.get("data").get("title"))
