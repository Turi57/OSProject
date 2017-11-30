#!/bin/bash

while true;
do
    ps -eo "cmd,%cpu" --sort=-%cpu | head -2 | tail -1
    sleep 3
done
