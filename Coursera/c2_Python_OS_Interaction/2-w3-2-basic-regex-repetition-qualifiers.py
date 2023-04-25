#!/usr/bin/env python3

import re

print(re.search(r"Py.*n", "Pygmalion"))
print("-----------------------------------")
# <re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py.*n", "Python Programming"))
print("-----------------------------------")
# <re.Match object; span=(0, 17), match='Python Programmin'>

print(re.search(r"Py[a-z]*n", "Python Programming"))
print("-----------------------------------")
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))
print("-----------------------------------")
# <re.Match object; span=(0, 3), match='Pyn'>

print(re.search(r"o+l+", "goldfish"))
print("-----------------------------------")
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly"))
print("-----------------------------------")
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))
print("-----------------------------------")
# None

print(re.search(r"p?each", "To each their own"))
print("-----------------------------------")
# <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like peaches"))
print("-----------------------------------")
# <re.Match object; span=(7, 12), match='peach'>

