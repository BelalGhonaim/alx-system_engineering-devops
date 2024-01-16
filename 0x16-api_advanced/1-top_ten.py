#!/usr/bin/python3
"""
unction that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):

    url_sub = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if url_sub.status_code >= 300:
        print('None')
    else:
        [print(titles.get("data").get("title"))
            for titles in url_sub.json().get("data").get("children")]