#!/usr/bin/env python3

import re

# * = cualquier numero de caracteres
# . = cualquier carácter
print(re.search(r".com", "welcome"))
print("-----------------------------------")
# <re.Match object; span=(2, 6), match='lcom'>

print(re.search(r"\.com", "welcome"))
print("-----------------------------------")
# None

print(re.search(r".com", "mydomain.com"))
print("-----------------------------------")
# <re.Match object; span=(8, 12), match='.com'>

print(re.search(r"\w*", "This is an example"))
print("-----------------------------------")
# <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "And_this_is_another."))
print("-----------------------------------")
# <re.Match object; span=(0, 19), match='And_this_is_another'>
