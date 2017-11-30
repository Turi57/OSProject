#!/bin/bash

RED='\033[0;31m'
NOCOLOR='\033[0m'

number=$(find \home -name "*.txt" -type f | wc -l)
echo -e "You have ${RED}$number ${NOCOLOR}txt files in your computer"

