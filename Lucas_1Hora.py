#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date, time, timedelta


# In[ ]:


final = datetime.now() + timedelta(hour = 1 )
hora_2 = final.hour

NewLucas = []
archivo = open("ListaNumeroNew.txt","w")

L0 = 2
L1 = 1

NewLucas.append(L0)
NewLucas.append(L1)

archivo.write(str(L0) + "\n")
archivo.write(str(L1) + "\n")

while(datetime.now().hour < hora_2):
    NewLucas.append(L0+L1)
    Ln = L0 + L1
    L0 = L1
    L1 = Ln
    #print(Ln)
    archivo.write(str(Ln) + "\n")

archivo.close()


# In[ ]:


archivo = open("ListaNumeroNew.txt","r")


archivo = open("ListaNumeroNew.txt","r")
ultimoNumero = open("NumeroFinal.txt","w")

archivo_lineas = archivo.readlines()
archivo.close()

ultima_linea = archivo_lineas[len(archivo_lineas)-1]

print(ultima_linea)

ultimoNumero.write(str(ultima_linea1))

ultimoNumero.close()

