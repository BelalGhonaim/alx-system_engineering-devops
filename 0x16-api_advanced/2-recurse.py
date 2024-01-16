#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):

    sub_url = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_url.status_code >= 404:
        return None

    count_hot_list = hot_list + [y.get("data").get("title")
                        for y in sub_url.json()
                        .get("data")
                        .get("children")]


    sub_resp = sub_url.json()
    if not sub_resp.get("data").get("after"):
        return count_hot_list


    return recurse(subreddit, count_hot_list, sub_resp.get("data").get("count"),
                   sub_resp.get("data").get("after"))
