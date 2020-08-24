#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        html = request.urlopen(sys.argv[1])
        print(html.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
