#!/usr/bin/python3
""" This module supplies a script that fetches a url """
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print('Body response:')
    print('\t- type: ' + str(type(content)))
    print('\t- content: ' + str(content))
    print('\t- utf8 content: ' + content.decode('utf-8'))
