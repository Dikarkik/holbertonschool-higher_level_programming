#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys
    data = {'q': ""}
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        r_dict = response.json()
        if len(r_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r_dict['id'], r_dict['name']))
    except:
        print("Not a valid JSON")
