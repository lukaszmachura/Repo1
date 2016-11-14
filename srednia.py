from math import sqrt
from myerror import *

def srednia(lista):
    """ Obliczanie sredniej kwadratowej """

    #Sprawdzenie czy input jest lista
    if type(lista)!=list:
        raise IBeBack;

    suma = 0.0
    for i in lista:
        suma += i**2
    return sqrt((suma/len(lista)))


def innaSrednia(lista):
    """ Srednia elementow listy """
    suma = 0.0
    for i in lista:
    suma += i
    return (suma/len(lista))
