from histogram import scanFile
from show_histogram import show_histogram
from znaki import oFile

#plik = 'To jest przykladowy tekst a to nie jest przykladowy tekst'
plik=oFile('file.txt')
h = scanFile(plik)
print '##################################################'
print h
print '##################################################'
print show_histogram(h)
print '##################################################'
