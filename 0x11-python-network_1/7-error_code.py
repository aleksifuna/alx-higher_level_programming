#!/usr/bin/python3
"""
sends a get request and check the status code
"""
import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print('Error code: ' + str(response.status_code))
    else:
        print(response.text)
