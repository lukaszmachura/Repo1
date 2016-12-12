import sys

alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
         "r","s","t","q","u","v","w","x","y","z"," ","A","B","C","D","E",
         "F","G","H","I","J","K","L","M","N","O","P","R","S","Q","T","U",
         "W","V","X","Y","Z"]

def znaki(text):

    table=[]
    for i in text:
        if i=="\n":
            i=" "
        if i in alfabet:
            table.append(i)
    return "".join(table)

def nope(fileName):
    with open('file.txt') as f:
        File = f.read()
        return znaki(File);
