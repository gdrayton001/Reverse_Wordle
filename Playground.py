from Fact import Fact

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

myList = [0,1,2,3,4,5,6,7,8,9]

for i in myList:
    if i % 2 == 0:
        myList.remove(i)
print(myList)