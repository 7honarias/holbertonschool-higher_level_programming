#!/usr/bin/python3
""" script that takes in a URL, sends
a request to the URL and displays the value of the
X-Request-Id variable found in the
header of the response
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    page = argv[1]
    with request.urlopen(page) as response:
        print(response.headers.get("X-Request-Id"))
