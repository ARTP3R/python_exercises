#!/bin/bash

# fruits.sh
# rename.sh
# toploglines.sh
# 2-w6-3-advanced-bash-for-loops.sh

for fruit in peach orange apple; do
    echo "I like $fruit!"
done

echo "Renombrar todos los ficheros htm a html"

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html"
done

echo "Buscar en el log de sistema"

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
