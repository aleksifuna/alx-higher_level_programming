#!/usr/bin/python3
""" This module supplies a script that posts to a url"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(content.decode('utf-8'))
