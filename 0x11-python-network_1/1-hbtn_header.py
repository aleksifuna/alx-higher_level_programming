#!/usr/bin/python3
""" This module supplies a script that fetches a url """
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    content = response.headers.get('X-Request-Id')
    print(content)
