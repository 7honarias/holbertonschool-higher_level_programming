#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    try:
        req = requests.get(url)
    except 
        print(req.status)
