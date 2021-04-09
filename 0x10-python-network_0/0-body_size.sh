#!/bin/bash
# script that takes in a URL
curl -sI "$1" | awk '/Content-length/{print $2}'