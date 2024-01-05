#!/bin/bash
# Takes in a URL, sends request to that URL, display body of response
curl -sI "$1" | grep -w 'Content-Length' | cut -f2 -d' '
