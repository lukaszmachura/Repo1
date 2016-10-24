from math import sqrt
from myerror import *

def srednia(lista):
    """ """
    if type(lista)!=list:
        raise IBeBack;

    suma = 0.0
    for i in lista:
        suma += i**2
    return sqrt((suma/len(lista)))
