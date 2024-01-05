#!/bin/bash
# shellcheck disable=SC2046
if [ $(curl -sLX HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
