#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    import requests

    num_of_sub = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headers={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)
    if num_of_sub.status_code >= 300:
        return 0


    return num_of_sub.json().get("data").get("subscribers")
