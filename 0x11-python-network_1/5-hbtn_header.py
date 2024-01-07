#!/usr/bin/python3
"""
supplies a function that fetches a variable in response header
"""
import sys
import requests


response = requests.get(sys.argv[1])
print(response.headers['X-Request-Id'])
