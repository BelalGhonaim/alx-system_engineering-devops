#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    url_sub = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    """ add requests module and add headers func """
    sub_response_info = requests.get(url_sub, headers=sub_headers, allow_redirects=False)
    if sub_response_info.status_code == 404:
        return 0
    response = sub_response_info.json().get("data")
    
    return response.get("subscribers")
