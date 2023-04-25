#!/usr/bin/env python3

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"

# \		caracter de escape para el corchete abierto
# [		corchete abierto literal en el texto
# (		paréntesis abierto para grupo de captura
# \d+	grupo de captura: coincidencia con uno o más caracteres numericos
# )		paréntesis cerrado para cierre de grupo de captura
# \		caracter de escape para el corchete cerrado
# ]		corchete cerrado literal en el texto


result = re.search(regex, log)
print(result[1])
print("-----------------------------------")
# 

result = re.search(regex, "A completely different string that also has numbers [532]")
print(result[1])
print("-----------------------------------")
# 

def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
