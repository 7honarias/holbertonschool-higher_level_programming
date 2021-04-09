#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            text = res.read().decode('utf8')
            print(text)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
