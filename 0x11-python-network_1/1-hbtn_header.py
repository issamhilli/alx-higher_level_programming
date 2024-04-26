#!/usr/bin/python3a
"""takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.

Usage: ./1-hbtn_header.py <URL>
"""
import sys

import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
