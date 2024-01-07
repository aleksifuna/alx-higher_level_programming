#!/usr/bin/python3
"""
supplies a function that fetches a variable in response header
"""
import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
