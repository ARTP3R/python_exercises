#!/usr/bin/env python3

# random_exit.py
# 2-w6-3-advanced-bash-while-loops.py

import sys
import random

value=random.randint(0, 3)
print("Returning: " + str(value))
sys.exit(value)
