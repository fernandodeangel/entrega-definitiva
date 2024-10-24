'''
Created on 24 oct 2024

@author: deang
'''
#ejercicio A

def P2(n, k, i=1):
    if n <= 0 or k <= 0 or i <= 0:
        raise ValueError
    if i>=k+1:
        raise ValueError
    if n<k:
        raise ValueError
    resultado = 1
    for j in range(i, k-1 + 1):
        resultado *= (n - j + 1)
    return resultado


#ejercicio B

import math 

def C2(n, k):
    if n<0:
        raise ValueError
    if k<0:
        raise ValueError
    return math.comb(n, k+1)


#ejercicio C

def S2(n, k):
    if n<=0 or k<=0:
        raise ValueError
    if n<k:
        raise ValueError
    factorial_k=math.factorial(k)
    factorial_k_mas_2=math.factorial(k + 2)
    
    sumatoria = 0 
       
    for i in range(k+1):
        signo=(-1)**i
        combinatorio=math.comb(k, i)
        potencia=(k-i) ** (n+1)
        sumatoria += signo * combinatorio * potencia

    resultado = (factorial_k / (n * factorial_k_mas_2)) * sumatoria
    return resultado


#ejercicio D
from collections import Counter
import re
def palabrasMasComunes(fichero, n=5):
    if n<=1:
        raise ValueError
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            texto=file.read().lower()
    except FileNotFoundError:
        raise FileNotFoundError
    palabras = re.findall(r'\b\w+\b', texto)
    contador = Counter(palabras)
    palabras_comunes = contador.most_common(n)
    return palabras_comunes

    
#Comprobaciones:
A: print(P2(6, 4))
B: print(C2(6, 4))
C: print(S2(6, 4))
nombre_fichero = "archivo_palabras.txt"
resultado=palabrasMasComunes(nombre_fichero)
D: print(resultado)
