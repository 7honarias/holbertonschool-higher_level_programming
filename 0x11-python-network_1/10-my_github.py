#!/usr/bin/python3
"""
Write a Python script that takes your
GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=HTTPBasicAuth(username, password))
    print(req.json().get('id'))
