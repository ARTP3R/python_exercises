#!/bin/bash

# retry.sh
# # 2-w6-3-advanced-bash-while-loops.sh

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done
echo -------------------------
n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;
