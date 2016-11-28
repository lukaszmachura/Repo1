File = open('file.txt').read()

def scanFile(text):
    wordArray = [ [],[] ]
    wordText = '';
    charCounter = 0;
    
    for i in text:
        
        if ( i == ' ') or ( i == '\n' ):
            if charCounter in wordArray[0]:
                idx = wordArray[0].index( charCounter );
                wordArray[1][idx] += 1;
            else:
                wordArray[0].append( charCounter );
                wordArray[1].append( 1 );
            
            #print wordText, charCounter
            wordText = '';
            charCounter = 0;
            continue;
        
        wordText += i;
        charCounter += 1;

    return wordArray;

table = scanFile( File );

for i in range( len(table[0])-1 ):
    print 'Slowo o ilosci', table[0][i], 'liter, wystepuje', table[1][i], 'razy.'
