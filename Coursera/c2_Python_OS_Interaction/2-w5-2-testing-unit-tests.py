#!/usr/bin/env python3

############################################
# Ejercicio: 2-w5-2-testing-unit-tests.py
# Ficheros: rearrange.py y rearrange_test.py
############################################

import re

def rearrange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	return "{} {}".format(result[2], result[1])

