#!/usr/bin/python3
"""Function that queries the Reddit API."""
import requests
import sys


def number_of_subscribers(subreddit):
    """Query the Reddit API to find the number of subscribers.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if the subreddit is invalid.
    """
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
