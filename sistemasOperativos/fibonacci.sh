#!/bin/bash

number=$1

a=1
b=0
fibo=0
for ((i = 0; i < number; i++))
do
    fibo=$((a+b))
    a=$b
    b=$fibo
    printf "%d " "$fibo"
done
printf "\n"

