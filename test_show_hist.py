from histogram import scanFile
from show_histogram import show_histogram

plik = 'To jest przykladowy tekst a to nie jest przykladowy tekst'
h = scanFile(plik)
print '##################################################'
print h
print '##################################################'
print show_histogram(h)
print '##################################################'
