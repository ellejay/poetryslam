import random

class PoetryBot:

    corpus = {}
    
    def readTextFromFile(self):
        f = open("innocence.txt", "r")
        sourceLines = []
        for line in f:
            sourceLines.append(line)
        return sourceLines

    def processSourceText(self):
        lines = self.readTextFromFile()
        poemAsLines = []
        for line in lines:
            lowercase = line.lower()
            newline = lowercase.split()
            if newline:
                newline.insert(0, '*S*')
                newline.append('*E*')
                poemAsLines.append(newline)
        return poemAsLines

    def textToDict(self):
        poemAsLines = self.processSourceText()
        corpus = {}
        for line in poemAsLines:
            word = iter(line)
            current = word.next()
            for nextWord in word:
                corpus.setdefault(current, []).append(nextWord)
                current = nextWord
        self.corpus = corpus

    def generateLine( self, corpus ):
        poem = []
        firstWords = corpus['*S*']
        firstWord = random.choice( firstWords )
        poem.append( firstWord )
        while poem[-1] != '*E*':
            poem.append(random.choice(corpus[poem[-1]]))
        poem = poem[:-1]
        return poem

    def generatePoem( self, stanzas, lines ):
        poem = []
        for x in range(0, stanzas):
            for y in range(0, lines):
                print ' '.join( self.generateLine( self.corpus ) ).capitalize()
            print ''

poetryGenerator = PoetryBot()
poetryGenerator.textToDict()
poetryGenerator.generatePoem( 3, 6 )
