#!/usr/bin/env python3

import subprocess

subprocess.run(["date"])
print("-----------------------------------")

print(subprocess.run(["date"]))
print("-----------------------------------")

subprocess.run(["sleep", "2"])
print("-----------------------------------")

print(subprocess.run(["sleep", "2"]))
print("-----------------------------------")

result = subprocess.run(["ls", "this_file_doesnt_exist"])
print("-----------------------------------")

print(subprocess.run(["ls", "this_file_doesnt_exist"]))
print("-----------------------------------")

