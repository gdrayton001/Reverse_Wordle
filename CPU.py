from Fact import Fact
import random
import sqlite3

factbook = {'a':Fact('a'),
            'b':Fact('b'),
            'c':Fact('c'),
            'd':Fact('d'),
            'e':Fact('e'),
            'f':Fact('f'),
            'g':Fact('g'),
            'h':Fact('h'),
            'i':Fact('i'),
            'j':Fact('j'),
            'k':Fact('k'),
            'l':Fact('l'),
            'm':Fact('m'),
            'n':Fact('n'),
            'o':Fact('o'),
            'p':Fact('p'),
            'q':Fact('q'),
            'r':Fact('r'),
            's':Fact('s'),
            't':Fact('t'),
            'u':Fact('u'),
            'v':Fact('v'),
            'w':Fact('w'),
            'x':Fact('x'),
            'y':Fact('y'),
            'z':Fact('z')}

conn = sqlite3.connect('words.db')
cursor = conn.cursor()

def clearMemory():
    for fact in factbook.values():
        fact.clearMemory()

def couldBe(word):
    for fact in factbook.values():
        if not fact.couldBe(word):
            return False
    return True

def generateGuess():
    cursor.execute("SELECT * FROM wordles;")
    words = cursor.fetchall()
    guess = random.choice(words)
    while not couldBe(guess):
        guess = random.choice(words)
    return guess

def learnFrom(findings):
    guess = ""
    colors = []
    for t in findings:
        guess += t[0]
        colors.append(t[1])
    for i in range(len(guess)):
        if colors[i] == "green":
            factbook[guess[i]].isInPos(i)
        elif colors[i] == "yellow":
            factbook[guess[i]].inWordButNotInPos(i)
        else:
            instances = 0
            for j in range(len(guess)):
                if j == i:
                    continue
                elif guess[j] == guess[i] and (colors[j] == "green" or colors[j] == "yellow"):
                    instances += 1
            if instances == 0:
                factbook[guess[i]].notInWord()
            else:
                factbook[guess[i]].officiateCountToBe(instances)