import sys

def scanFile(text):
    
    histogram = {}
    split_text = text.split(" ")
    
    for wyraz in split_text:
        if len(wyraz) in histogram:
            histogram[len(wyraz)] += 1
        else:
            histogram[len(wyraz)] = 1
    
    return histogram

        
if len(sys.argv) == 1:
    file_name = 'file.txt'
else:
    file_name = sys.argv[1]

with open(file_name) as f:
    File = f.read()
    print scanFile(File);
