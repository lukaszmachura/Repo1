from histogram import scanFile
from histogram import openFile
from show_histogram import show_histogram

plik = 'file.txt'
h = openFile(plik)
print '##################################################'
print h
print '##################################################'
print show_histogram(h)
print '##################################################'
