import string

letters = list(string.ascii_lowercase)
code = ""

codeword = input().lower()

for l in codeword:
    if letters.index(l) < 10:
        char = str(letters.index(l))
    else:
        char = letters[letters.index(l) - 10]
    code += char
    
print(code)