#!/bin/bash
# displays the status code of a response from a server
curl -o /dev/null -sw "%{http_code}" "$1"
