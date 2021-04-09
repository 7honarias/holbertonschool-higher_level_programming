#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an
email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    url = argv[1]
    mail = argv[2]
    values = {'email': mail}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf8")
        print(the_page)
