File = open('file.txt').read()

def scanFile(text):
    wordText = '';
    charCounter = 0;
    
    for i in text:
        
        if ( i == ' ') or ( i == '\n' ):
            print wordText, charCounter
            wordText = '';
            charCounter = 0;
            continue;
        
        wordText += i;
        charCounter += 1;

scanFile( File );
