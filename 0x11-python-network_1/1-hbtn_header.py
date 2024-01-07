#!/usr/bin/python3
""" This module supplies a script that fetches a url """
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.headers.get('X-Request-Id')
    print(content)
