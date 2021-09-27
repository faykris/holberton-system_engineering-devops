#!/usr/bin/python3
"""0. How many subs? - Module"""
import json

def number_of_subscribers(subreddit):
    import urllib
    with urllib.request.urlopen(
            ' https://www.reddit.com/dev/api/subreddits/mine/subscriber/') as response:
        html2 = response.read()
    user_d = html2.decode('utf-8')
    user_dict = json.loads(user_d)
    return user_dict
