#!/usr/bin/python3
"""2. Recurse it!"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """recurse - returns a list containing the titles of all hot articles"""
    import requests

    response = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Mozilla",
                     "Content-Type": "application/json"},
            params={"count": count, "after": after},
            allow_redirects=False,
    )
    if response.status_code > 399:
        return None

    obj_list = response.json()
    for ele in obj_list.get("data").get("children"):
        if ele.get("data").get("title"):
            hot_list.append(ele.get("data").get("title"))

    data = response.json()
    if not data.get("data").get("after"):
        return hot_list

    return recurse(subreddit, hot_list,
                   data.get("data").get("count"),
                   data.get("data").get("after")
                   )
