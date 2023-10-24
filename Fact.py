class Fact:
    
    letter = ''
    possiblePos = []
    defPos = []
    inWord = None
    minCount = 0
    knowCount = False
    
    def __init__(self, letter):
        self.letter = letter
        self.possiblePos = [0,1,2,3,4]
        self.defPos = []
    
    def clearMemory(self):
        self.possiblePos = [0,1,2,3,4]
        self.defPos.clear()
        self.inWord = None
        self.minCount = 0
        self.knowCount = False
        
    def couldBe(self, word):
        if self.inWord == None:
            return True
        elif self.inWord:
            for pos in self.defPos:
                if word[pos] != self.letter:
                    return False
            for i in range(len(word)):
                if word[i] == self.letter and i not in self.possiblePos:
                    return False
            if word.count(self.letter) < self.minCount:
                return False
            elif word.count(self.letter) > self.minCount and self.knowCount:
                return False
            return True
        else:
            if self.letter in word:
                return False
            return True
        
    def inWordButNotInPos(self, index):
        if index > 4:
            raise IndexError
        if index not in self.possiblePos:
            return
        self.inWord = True
        self.possiblePos.remove(index)
        
    def isInPos(self, index):
        if index > 4:
            raise IndexError
        if index in self.defPos:
            return
        self.defPos.append(index) 
        self.inWord = True  
        
    def notInWord(self):
        self.possiblePos.clear()
        self.inWord = False
        self.knowCount = True
        
    def officiateCountToBe(self, count):
        self.minCount = count
        self.knowCount = True
        self.inWord = True
                
    def setCount(self, count):
        self.minCount = count