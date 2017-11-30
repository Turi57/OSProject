#!/bin/bash
tput sc

while true; do
    for char in '-' '\' '|' '/'; do
        tput rc
        printf "%s" "$char"
        sleep 0.2
    done
done

