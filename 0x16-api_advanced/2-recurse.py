#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):

    sub_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    sub_head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    para = {
        "after": after,
        "count": count,
        "limit": 100
    }
    sub_resp = requests.get(sub_url, headers=sub_head, params=para,
                            allow_redirects=False)
    if sub_resp.status_code == 404:
        return None

    response = sub_resp.json().get("data")
    after = response.get("after")
    count += response.get("dist")
    for c in response.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after > 0:
        return recurse(subreddit, hot_list, after, count)
    return hot_list