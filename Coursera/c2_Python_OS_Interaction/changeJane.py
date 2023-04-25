#!/usr/bin/env python3

import sys
import os
from pathlib import Path

with open (sys.argv[1], "r") as my_file:
    for line in my_file:
		data= line.replace("\n", "")
		base=os.path.basename(data)
		base_new = base.replace("jane", "jdoe")
		os.chdir('/home/student-01-6058459fd40f/data')
		os.rename(base, base_new)
my_file.close()