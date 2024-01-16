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

<<<<<<< HEAD

    sub_resp = sub_url.json()
    if not sub_resp.get("data").get("after"):
        return count_hot_list


    return recurse(subreddit, count_hot_list, sub_resp.get("data").get("count"),
                   sub_resp.get("data").get("after"))
=======
    if after > 0:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
>>>>>>> d67efd7d70267f816930a93e67364966f6b65759
