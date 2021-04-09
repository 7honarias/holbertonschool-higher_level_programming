#!/bin/bash
# script that takes in a URL
curl -sI "$1" | awk '/Content-Length/{print $2}'
