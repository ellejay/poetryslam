import json
import random
from pprint import pprint
from string import punctuation

class PoetryBot:

    def __init__( self, filePath  ):
        self.corpus = {}
        self.addToCorpus( filePath )

    def addToCorpus( self, filePath ):
        poemAsLines = self.processSourceText( filePath )
        for line in poemAsLines:
            word = iter( line )
            current = word.next()
            for nextWord in word:
                self.corpus.setdefault(current.lower(), []).append( nextWord )
                current = nextWord

    def processSourceText( self, filePath ):
        poemAsLines = []
        data = json.load( open( filePath ) )
        for poem in data:
            lines = poem['text']
            for line in lines:
                newline = line.split()
                if newline:
                    newline.insert( 0, '*s*' )
                    newline.append( '*e*' )
                    poemAsLines.append( newline )
        return poemAsLines

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

poetryGenerator = PoetryBot('shelley.json')
poetryGenerator.generatePoem(1, 10)
poetryGenerator.generatePoem(2, 4)


