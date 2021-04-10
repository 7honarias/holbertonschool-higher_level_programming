#!/usr/bin/python3
"""
The Holberton School staff evaluates
candidates applying for a back-end
position with multiple
technical challenges, like this one:
"""
if __name__ == "__main__":
    import sys
    import requests
    repo = sys.argv[1]
    owner = sys.argv[2]
    response = requests.get("https://api.github.com/repos/{}/{}/commits"
                           .format(owner, repo))
    commits = response.json()
    for commit in commits:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
