def sprawdzListe(lista):
    """ lista jest lista i krotka a elementy sa liczbami """

    ret = False

    if (type(lista) is list) or (type(lista) is tuple):
	for i in lista:
	    if (type(i) is int) or (type(i) is float):
		ret = True
	    else:
		return False
    else:
	return False

    return ret