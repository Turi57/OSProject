#!/bin/bash

number=$1
a=1
b=0

if [ $# -ne 1 ];
then
    echo "Correct usage: ./fibonacci.sh [number of terms]"
    exit 1
fi

for ((i=0; i < number; i++))
do
    fibo=$((a+b))
    a=$b
    b=$((fibo))
    printf "%d " "$fibo"
done
printf "\n"
