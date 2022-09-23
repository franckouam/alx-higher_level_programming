#!/bin/bash
# Displays only the status code of a given request
curl -sLw "%{status_code}" -o /dev/null "$1"
