#!/usr/bin/env python3

import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# encuentra la primera palabra de 5 letras
print("-----------------------------------")
# <re.Match object; span=(2, 7), match='ghost'>

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# encuentra la primera palabra de 5 letras
print("-----------------------------------")
# <re.Match object; span=(2, 7), match='scary'>

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# encuentra TODAS (findall) las "palabras" contenidas con 5 letras
print("-----------------------------------")
# ['scary', 'ghost', 'appea']

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
# encuentra TODAS las palabras de exactamente 5 letras
# regex delimitada mediante \b
print("-----------------------------------")
# ['scary', 'ghost']

print(re.findall(r"\w{5,10}", "a scary ghost appeared, i really like strawberries"))
# encuentra TODAS las palabras contenidas de 5 a 10 letras
print("-----------------------------------")
# ['scary', 'ghost', 'appeared', 'really', 'strawberri']

print(re.findall(r"\b\w{5,10}\b", "a scary ghost appeared, i really like strawberries"))
# encuentra TODAS las palabras exactamente de 5 a 10 letras
print("-----------------------------------")
# ['scary', 'ghost', 'appeared', 'really']

print(re.search(r"s\w{,20}", "i really like strawberries"))
# palabras que empiecen por s y de hasta 20 letras
print("-----------------------------------")
# <re.Match object; span=(14, 26), match='strawberries'>

import re
def long_words(text):
  pattern = (r"\w{7,}")
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


