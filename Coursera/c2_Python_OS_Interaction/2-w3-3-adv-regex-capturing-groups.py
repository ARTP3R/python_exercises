#!/usr/bin/env python3

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# busca caracteres a la izquierda de una coma y a la derecha de la coma


print(result)
print("-----------------------------------")
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

print(result.groups())
print("-----------------------------------")
# ('Lovelace', 'Ada')

print(result[0])
print("-----------------------------------")
# Lovelace, Ada

print(result[1])
print("-----------------------------------")
# Lovelace

print(result[2])
print("-----------------------------------")
# Ada

print("{} {}".format(result[2], result[1]))
print("-----------------------------------")
# Ada Lovelace

def rearrange_name(name):
	rn_result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
	if rn_result is None:
		return name
	return "{} {}". format(rn_result[2], rn_result[1])

print(rearrange_name("Lovelace, Ada"))
# Ada Lovelace
print(rearrange_name("Ritchie, Dennis"))
# Dennis Ritchie
print(rearrange_name("Hopper, Grace M."))
# Grace M. Hopper