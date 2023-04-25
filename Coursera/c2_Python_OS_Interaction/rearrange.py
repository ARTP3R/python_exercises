#!/usr/bin/env python3

############################################
# Ejercicio: 2-w5-2-testing-unit-tests.py
# Ficheros: rearrange.py y rearrange_test.py
############################################


import re

def rearrange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)

############################################
# Ejercicio: 2-w5-2-testing-edge-cases.py
############################################

	if result is None:
		return name

############################################

	return "{} {}".format(result[2], result[1])

