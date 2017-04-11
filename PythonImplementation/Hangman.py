import sys
import os
numLetters = 0
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' ,
            'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' ,
            'u' , 'v' , 'w' , 'x' , 'y' , 'z' , '\n']
guessCounter = 0
guessedLetters = ['0' , '0' , '0' , '0' , '0' , '0', '0' ,'0' ,'0' ,'0' ,'0' ,'0' , '0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' , '0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0']
totals = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
frequencies = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]

def isGuessed(letter) :
    global guessedLetters
    for i in range(26) :
        if guessedLetters[i] == letter :
            return 1
    return 0

def getGuess() :
    global totals
    global letters
    global frequencies
    totals = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
    frequencies = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
    filePath = "TempDict.txt"
    f = open("TempDict.txt" , "r")
    d = f.readlines()
    if len(d) == 0 :
        print("Error, no words found.\n")
        sys.exit()
    if len(d) == 1 :
        for i in d :
            f.close()
            return i
    total = 0
    for i in d :
        for c in i :
            if c != '\n' :
                for l in range(26) :
                    if letters[l] == c :
                        totals[l] = totals[l] + 1
                        total = total + 1
    for l in range(26) :
        frequencies[l] = totals[l]/total
    maxIndex = 0
    maxValue = 0
    for l in range(26) :
        if isGuessed(letters[l]) == 0 :
            if frequencies[l] > maxValue :
                maxIndex = l
                maxValue = frequencies[l]
    f.close()
    return letters[maxIndex]


def makeDictionary(num) :
    f = open("../Words.txt" , "r")
    f2 = open("TempDict.txt" , "a")
    d = f.readlines()
    f2.seek(0)
    for i in d :
        k = len(i)
        if k == num - 1 :
            f2.write(i)
    f2.truncate
    f2.close()
    f.close()

def start() :
    global numLetters
    numLetters = eval(input("How many letters? : "))
    print("numLetters : {}\n".format(numLetters))
    if numLetters < 4 :
        print("Please enter a number >= 4.\n")
        sys.exit() 
    makeDictionary(numLetters + 2)

def removeWords(letter , position) :
    f = open("TempDict.txt" , "r+")
    d = f.readlines()
    f.seek(0)
    for i in d :
        if i[position - 1] == letter :
            print("position {} in word {} is letter {}".format(position , i , letter))
            f.write(i)
    f.truncate()
    f.close()

def removeWord(letter) :
    f = open("TempDict.txt" , "r+")
    d = f.readlines()
    f.seek(0)
    for i in d :
        found = 0
        for c in i :
            if c == letter :
                found = 1
        if found == 0 :
            f.write(i)
    f.truncate()
    f.close()

def isevaluable(s):
    try:
        eval(s)
        return True
    except:
        return False

def removeWordsWithLetterInPos(letter , pos) :
    global numLetters
    if pos == 0 :
        return
    if pos > numLetters :
        return
    f = open("TempDict.txt" , "r+")
    d = f.readlines()
    f.seek(0)
    for i in d :
        if i[pos - 1] == letter :
            print("Found word : {} contains letter {} in {} pos.\n".format(i , letter , pos - 1))
        if i[pos - 1] != letter :
            f.write(i)
    f.truncate()
    f.close()

try :
    os.remove("TempDict.txt")
except OSError :
    pass
start()
solved = 0
while solved == 0 :
    letter = getGuess()
    if len(letter) != 1 :
        print("Your word is : {}".format(letter))
        sys.exit()
    print("I guess.... {}!.".format(letter))
    guessedLetters[guessCounter] = letter
    guessCounter = guessCounter + 1
    val = "text"
    vals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    counter = 0
    while val != "done" and val != "no" :
        val = input()
        if val != "done" and val != "no" :
            if isevaluable(val) :
                if eval(val) > 0 and eval(val) <= numLetters :
                    vals[counter] = eval(val)
                    counter = counter + 1
                else :
                    print("Please enter a value between 1 and {}\n".format(numLetters))
            else :
                print("Please enter a value between 1 and {}\n".format(numLetters))
        elif val == "done" and counter == 0 :
            val = "text"
            print("Please enter 'no' or at least one index.\n")

    if val != "no" :
        tempVals = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        for i in range(len(vals)) :
            if vals[i] != 0 :
                print("vals[i] : {}\n".format(vals[i]))
                tempVals[vals[i]] = 0
                removeWords(letter , vals[i])
        for i in tempVals :
            removeWordsWithLetterInPos(letter , i)
    if val == "no" :
        removeWord(letter)





