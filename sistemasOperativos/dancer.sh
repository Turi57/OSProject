#!/bin/bash
tput civis

#trap 'tput cnorm; echo' EXIT
#trap 'exit 127' HUP INT TERM

#let columns=$(tput cols)
let current=1

while true; do
    for char in '-' '\' '|' '/'; do
        let columns=$(tput cols)
        if ((current>columns))
        then
            tput cud1
            let current=1
        fi
        tput sc
        printf "%s" "$char"
        sleep 0.05
        tput rc
        printf " "
        let current=current+1
    done
done
