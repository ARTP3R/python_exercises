

milista=[1, True, 1.1, "María", "Pepe", "Marta", "Antonio", "B", "C", "D", "E"]
print("Lista ", milista[:])
print("")

milista.append("triángulo")
print("milista.append(\"triángulo\")")
print("Lista ", milista[:])
print("")

milista.insert(2,"Sandra")
print("milista.insert(2,\"Sandra\")")
print("Lista ", milista[:])
print("")

milista.extend(["Sandía", "Ana", "Lucía"])
print("milista.extend([\"Sandía\", \"Ana\", \"Lucía\"])")
print("Lista ", milista[:])
print("")

print("print(milista[1:5])")
print(milista[1:5])
print("")

print("print(milista.index(\"triángulo\"))")
print(milista.index("triángulo"))
print("")

print("print(\"Pepe\" in milista)")
print("Pepe" in milista)
print("")

print(milista[2])
print("print(milista[2])")
print("")

milista.remove("Ana")
print("milista.remove(\"Ana\")")
print(milista[:])
print("")

milista.remove(1)
print("milista.remove(1)")
print(milista[:])
print("")

milista.pop()
print("milista.pop()")
print(milista[:])
print("")


milista2=["teta", "culo", "chochete"]
print("milista2=[\"teta\", \"culo\", \"chochete\"]")
milista3=milista+milista2*3
print("milista3=milista+milista2*3")
print("print(milista3[:])")
print(milista3[:])
print("")