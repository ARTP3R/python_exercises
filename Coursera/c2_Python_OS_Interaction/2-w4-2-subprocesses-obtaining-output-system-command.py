#!/usr/bin/env python3

# REQUIERE VERSION 3.7.3

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

# código de salida
print(result.returncode)
# 0
print("-------------------------------------------------")

# salida del comando (en bytes, no apta para python, por eso la )
print(result.stdout)
# b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
print("-------------------------------------------------")

# salida decodificada UTF-8
print(result.stdout.decode())
# 8.8.8.8.in-addr.arpa domain name pointer dns.google.
print("-------------------------------------------------")

# salida decodificada UTF-8, convertida en lista separando por espacios
print(result.stdout.decode().split())
# 8.8.8.8.in-addr.arpa domain name pointer dns.google.
print("-------------------------------------------------")
print("=================================================")

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print("-------------------------------------------------")
print(result.stdout)
print("-------------------------------------------------")
print(result.stderr)
print("-------------------------------------------------")
print(result.stderr.decode())
print("-------------------------------------------------")
print("=================================================")

result = subprocess.run(["who"], capture_output=True)

print("-------------------------------------------------")
print(result.returncode)
print("-------------------------------------------------")
print(result.stdout)
print("-------------------------------------------------")
print(result.stdout.decode())
print("-------------------------------------------------")