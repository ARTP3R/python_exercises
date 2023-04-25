#!/usr/bin/env python3

import re

print(re.search(r"[Pp]ython", "Python"))
print("-----------------------------------")
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way", "The end of the highway"))
print("-----------------------------------")
# <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go"))
print("-----------------------------------")
# None

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print("-----------------------------------")
# <re.Match object; span=(0, 6), match='cloudy'>

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print("-----------------------------------")
# <re.Match object; span=(0, 6), match='cloud9'>

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print("-----------------------------------")
# <re.Match object; span=(4, 5), match=' '>

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
print("-----------------------------------")
# <re.Match object; span=(30, 31), match='.'>

print(re.search(r"cat|dog", "I like cats."))
print("-----------------------------------")
# <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dog", "I like dogs."))
print("-----------------------------------")
# <re.Match object; span=(7, 10), match='dog'>

print(re.search(r"cat|dog", "I like both dogs and cats."))
print("-----------------------------------")
# <re.Match object; span=(12, 15), match='dog'>

print(re.findall(r"cat|dog", "I like both dogs and cats."))
print("-----------------------------------")
# ['dog', 'cat']
