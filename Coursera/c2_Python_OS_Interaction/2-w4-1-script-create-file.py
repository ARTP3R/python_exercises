#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
	with open(filename, "w") as f:
		f.write("New file created\n")

else:
	print("Error, the file {} already exists! ANDEVACOHONEEEE".format(filename))
	sys.exit(1)