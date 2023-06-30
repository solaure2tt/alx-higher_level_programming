#!/bin/bash
# displays the body of the 200 ok respons
res=$(curl -sI "$1" | grep 'HTTP' | cut -d' ' -f2); if [[ $res -eq 200 ]]; then curl -s "$1" -o t && cat t; fi
