#!/bin/bash
# Sends a GET request to a given URL and display de body of the response
curl -sL -d "X-School-User-Id"=98 -G "$1"
