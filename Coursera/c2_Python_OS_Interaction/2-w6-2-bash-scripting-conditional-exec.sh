#!/bin/bash

line="-----------------------------"

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

echo $line
echo "Test 1"

if test -n "$PATH"; then echo "Your path is not empty"; fi

echo $line
echo "Test 2"

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
