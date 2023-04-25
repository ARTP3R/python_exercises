#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# Para que la variable FRUIT aparezca en el entorno:
# user@maquina:~$ export FRUIT=Pinneaple