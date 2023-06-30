#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response
res=$(curl -sI "$1" | grep 'HTTP' | cut -d' ' -f2); if [[ $res -eq 200 ]]; then curl -s "$1" -o t && cat t; fi
