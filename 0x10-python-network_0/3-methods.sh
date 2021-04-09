#!/bin/bash
# script that takes in a URL
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
