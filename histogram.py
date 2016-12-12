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


def openFile(fileName):
    with open(fileName) as f:
        File = f.read()
        print scanFile(File);
