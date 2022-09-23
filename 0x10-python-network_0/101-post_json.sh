#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sL -d "@$2" -H "Content-type: application/json" "$1"
