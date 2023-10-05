from tkinter import *
import CPU
import enchant
import sqlite3
import string

root = Tk()
root.title("Reverse Wordle")
#root.geometry("500x400")

dictionary = enchant.Dict("en_US")

conn = sqlite3.connect('words.db')
cursor = conn.cursor()

try:  
    cursor.execute("CREATE TABLE wordles (one text, two text, three text, four text, five text)")
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                for d in string.ascii_lowercase:
                    for e in string.ascii_lowercase:
                        if dictionary.check(a+b+c+d+e):
                            print(a+b+c+d+e)
                            cursor.execute("INSERT INTO wordles VALUES (:one, :two, :three, :four, :five)", {'one':a, 'two':b,'three':c,'four':d,'five':e})
    conn.commit()
    conn.close()
except sqlite3.OperationalError:
    pass

def generate_guess():
    global score
    global winning_label
    guess = CPU.generateGuess()
    guess_labels = []
    findings = []  
    score += 1
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            color = "green"
        elif guess[i] in answer:
            if guess.count(guess[i]) <= answer.count(guess[i]):
                color = "yellow"
            else:
                coloredSpaces = 0
                for j in range(len(guess)):
                    if j == i:
                        continue
                    elif guess[j] == guess[i] and (guess[j] == answer[j] or j < i):
                        coloredSpaces += 1
                if coloredSpaces < answer.count(guess[i]):
                    color = "yellow"
                else:
                    color = "red"
        else:
            color = "red"
        guess_label = Label(root, text=guess[i], fg=color)
        guess_label.grid(row=2+len(guess_labels_array), column=i)
        guess_labels.append(guess_label)
        findings.append((guess[i], color))
    guess_labels_array.append(guess_labels)
    score_label.config(text="Score: " + str(score))
    CPU.learnFrom(findings)
    if "".join(guess) == answer:
        winning_label = Label(root, text="Great Job! Your score was " + str(score) + ". Play Again?")
        winning_label.grid(row=3+len(guess_labels_array), column=0, columnspan=5)
        generate_guess_button.config(text="Play Again", command=play_again)
    #for letter in guess:
        #print(CPU.factbook[letter].letter)
        #print("possiblePos: " + str(CPU.factbook[letter].possiblePos))
        #print("defPos: " + str(CPU.factbook[letter].defPos))
        #print("inWord: " + str(CPU.factbook[letter].inWord))
        #print("minCount: " + str(CPU.factbook[letter].minCount))
        #print("knowCount: " + str(CPU.factbook[letter].knowCount))

def play_again():
    global score
    score_label.grid_forget()
    generate_guess_button.grid_forget()
    winning_label.grid_forget()
    for myList in guess_labels_array:
        for label in myList:
            label.grid_forget()
    CPU.clearMemory()
    guess_labels_array.clear()
    enter_word_label.config(text="Enter Word for Me to Guess")
    enter_word_label.grid(row=0, column=0)
    word_entry.grid(row=1, column=0)
    submit_word_button.grid(row=2, column=0)    
    word_entry.delete(0, END)
    score = 0

def submit_word():
    global score_label
    global generate_guess_button
    global answer
    if not dictionary.check(word_entry.get()) or len(word_entry.get()) != 5:
        enter_word_label.config(text="Must be a word and be 5 letters long")
        return
    enter_word_label.grid_forget()
    word_entry.grid_forget()
    submit_word_button.grid_forget()
    score_label = Label(root, text="Score: " + str(score))
    generate_guess_button = Button(root, text="Generate Guess", command=generate_guess)
    answer = word_entry.get()
    score_label.grid(row=0, column=0, columnspan=5)
    generate_guess_button.grid(row=1, column=0, columnspan=5)

enter_word_label = Label(root, text="Enter Word for Me to Guess")
word_entry = Entry(root)
submit_word_button = Button(root, text="Submit", command=submit_word)
guess_labels_array = []
score = 0

enter_word_label.grid(row=0, column=0)
word_entry.grid(row=1, column=0)
submit_word_button.grid(row=2, column=0)

root.mainloop()