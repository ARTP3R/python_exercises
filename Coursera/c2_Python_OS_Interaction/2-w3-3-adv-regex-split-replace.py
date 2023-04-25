#!/usr/bin/env python3

import re

split_var = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(split_var)
print("-----------------------------------")
# ['One sentence', ' Another one', ' And the last one', '']

split_var2 = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(split_var2)
print("-----------------------------------")
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

replace_var = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts@my.example.com")
# [\w.%+-] alfanuméricos y _ y también . % + -
print(replace_var)
print("-----------------------------------")
# Received an email for [REDACTED]

replace_var2 = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# Paréntesis dos grupos de captura separados por coma
# r"\2 \1"      Parámetro. Indica orden grupos captura.
# 

print(replace_var2)
print("-----------------------------------")
# Ada Lovelace


example = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(example)
print("-----------------------------------")
# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']
