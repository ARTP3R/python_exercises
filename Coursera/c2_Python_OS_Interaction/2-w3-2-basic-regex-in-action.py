#!/usr/bin/env python3

import re

print(re.search(r"A.*a", "Argentina"))
print("-----------------------------------")
# <re.Match object; span=(0, 9), match='Argentina'>

print(re.search(r"A.*a", "Azerbaijan"))
print("-----------------------------------")
# <re.Match object; span=(0, 9), match='Azerbaija'>

print(re.search(r"^A.*a$", "Azerbaijan"))
print("-----------------------------------")
# None

print(re.search(r"^A.*a$", "Australia"))
print("-----------------------------------")
# <re.Match object; span=(0, 9), match='Australia'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name"))
print("-----------------------------------")
# <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>

print(re.search(pattern, "this isn't a valid variable name"))
print("-----------------------------------")
# None

print(re.search(pattern, "my_variable1"))
print("-----------------------------------")
# <re.Match object; span=(0, 12), match='my_variable1'>

print(re.search(pattern, "2my_variable1"))
print("-----------------------------------")
# None

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][A-Za-z\s]+[\.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True