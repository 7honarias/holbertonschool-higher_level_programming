#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    req = requests.post(url, data=data)
    try:
        res = req.json()
        id = res.get("id")
        name = res.get("name")
        if len(res) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
