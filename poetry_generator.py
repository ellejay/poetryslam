import json
import random
from pprint import pprint
from string import punctuation

class PoetryBot:

    corpus = {}
    filePath = ''

    def __init__( self, filePath  ):
        self.filePath = filePath
        self.createDictionary()

    def processSourceText( self ):
        poemAsLines = []
        data = json.load( open( self.filePath ) )
        for poem in data:
            lines = poem['text']
            for line in lines:
                newline = line.split()
                if newline:
                    newline.insert( 0, '*s*' )
                    newline.append( '*e*' )
                    poemAsLines.append( newline )
        return poemAsLines

    def createDictionary( self ):
        poemAsLines = self.processSourceText()
        corpus = {}
        for line in poemAsLines:
            word = iter( line )
            current = word.next()
            for nextWord in word:
                corpus.setdefault(current.lower(), []).append( nextWord )
                current = nextWord
        self.corpus = corpus

    def generateLine( self ):
        poemLine = []
        poemLine.append( random.choice( self.corpus['*s*'] ).capitalize() )
        while poemLine[-1] != '*e*':
            poemLine.append( random.choice( self.corpus[ poemLine[-1].lower() ] ) )
        poemLine = poemLine[:-1]
        return poemLine

    def generatePoem( self, stanzas, lines ):
        poem = []
        for x in range( 0, stanzas ):
            for y in range( 0, lines ):
                line = ' '.join( self.generateLine() )
                print line.strip( punctuation )
            print ''

poetryGenerator = PoetryBot('angelou.json')
poetryGenerator.generatePoem(2, 8)


