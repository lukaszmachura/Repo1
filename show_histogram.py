def show_histogram(inputHistogram, znak="="):
    """drukowanie histogramu w konsoli"""
    wynik = ""
    histogram = sorted(inputHistogram.keys())

    for index in histogram:
        ilosc = inputHistogram[ index ]
        bar = znak * ilosc

        tmp = str(index) + bar + '\n'
        
        wynik += tmp
    return wynik
