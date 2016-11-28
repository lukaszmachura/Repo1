from histogram import scanFile
from show_histogram import show_histogram

plik = 'file.txt'
h = scanFile(plik)
print "test"
print h
print show_histogram(h)


print show_histogram(dict(zip(range(10), range(20, 30))))