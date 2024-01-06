#!/bin/bash
# makes a request to a server and causes it to respond
curl -o /dev/null -sw "You find me!" 0.0.0.0:5000/catch_me
