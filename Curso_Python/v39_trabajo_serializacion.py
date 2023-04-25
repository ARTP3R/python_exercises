#!/usr/bin/python3

import pickle

lista_nombres=["Pedro", "Ana", "María", "Isabel"]

fichero_binario=open("v39_lista_nombres.bin","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()




fichero=open("v39_lista_nombres.bin","rb")

lista=pickle.load(fichero)

print(lista)