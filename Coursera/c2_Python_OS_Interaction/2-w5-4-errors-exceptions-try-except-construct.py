#!/usr/bin/env python3


# MAL
import os

def read_file(filename):
	if not os.path.exists(filename):
		return ""
	if not os.path.isfile(filename):
		return ""
	if not os.access(filename, os.R_OK):
		return ""
	if is_locked(filename):
		return ""
	if is_not_accessible(filename):
		return ""


# BIEN
def character_frequency(filename):
	"""Counts the frequency of each character in the given file."""
	# First try to open the file
	try:
		f = open(filename)
	except OSError:
		return None

	# Now process the file
	characters = {}
	for line in f:
		for char in line:
			characters[char] = characters.get(char, 0) + 1
	f.close()
	return characters