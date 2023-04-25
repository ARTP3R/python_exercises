#!/usr/bin/env python3

import os 
import subprocess

new_env = os.environ.copy()
new_env["PATH"] = os.pathsep.join(["/opt/myapp/", new_env[PATH]])

result = subprocess.run(["myapp"], env=new_env)

# Otros parámetros
# cwd -> para cambiar el current working directory
# timeout -> para limitar el tiempo del proceso
# shell ->