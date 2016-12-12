from math import ceil

def show_histogram(inputHistogram, znak="="):
    """drukowanie histogramu w konsoli"""
    wynik = ""
    histogram = sorted(inputHistogram.keys())

    for index in histogram:
        ilosc = inputHistogram[ index ]
        if (ilosc < 80):
            bar = znak * int( ceil( float(ilosc)%80 ) )
        else:
            bar = znak * int( ceil( float(ilosc)/80 ) )

        tmp = str(index) + bar + '\n'
        
        wynik += tmp
    return wynik
