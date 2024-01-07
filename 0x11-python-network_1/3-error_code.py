#!/usr/bin/python3
"""
This module supplies a script that sends a GET request and handles errors
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ' + str(e.code))
