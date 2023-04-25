#!/bin/bash

# rename.sh
# 2-w6-3-advanced-bash-for-loops.sh

for fruit in peach orange apple; do
    echo "I like $fruit!"
done

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html"
done
