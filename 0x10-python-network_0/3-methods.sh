#!/bin/bash
# displays the http methods the server will accept
curl -sLI ALLOW "$1" | grep 'Allow:' | cut -f2- -d' '
