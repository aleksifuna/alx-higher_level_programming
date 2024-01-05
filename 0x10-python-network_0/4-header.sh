#!/bin/bash
# sends a Get request with a header variable
curl -sLX GET "$1" - H "X-School-User-Id: 98"
