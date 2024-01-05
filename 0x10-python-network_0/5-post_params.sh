#!/bin/bash
# takes URL and sends POST with data
curl -sLX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
