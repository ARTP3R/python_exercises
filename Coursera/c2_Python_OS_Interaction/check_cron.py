#!/usr/bin/env python3

import re
import sys

# Guardar como check_cron.py
# No funciona con REPL. Hay que ejecutarlo como script.


print(sys.argv)
logfile = sys.argv[1]

usernames = {}

with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)