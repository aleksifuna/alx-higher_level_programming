#!/bin/bash
# sends a JSON POST request to a URL passed
curl -sLX POST "$1" -H "Content-Type: application/json" -d @"$2"
