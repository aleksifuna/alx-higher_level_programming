#!/usr/bin/python3
""" This module supplies a script that fetches a url """
import requests
response = requests.get('https://alx-intranet.hbtn.io/status')
content = response.text
print('Body response:')
print('\t- type: ' + str(type(content)))
print('\t- content: ' + str(content))
