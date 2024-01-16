#!/usr/bin/python3
"""
unction that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    sub_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    sub_head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    title_limits = {
        "limit": 10
    }
    sub_res = requests.get(sub_url, headers=sub_head, params=title_limits,
                            allow_redirects=False)
    if sub_res.status_code == 404:
        print("None")
        return
    output = sub_res.json().get("data")
    [print(y.get("data").get("title")) for y in output.get("children")]