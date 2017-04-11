import sys
numLetters = 0
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' ,
            'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' ,
            'u' , 'v' , 'w' , 'x' , 'y' , 'z' , '\n']
totals = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
frequencies = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
def getGuess() :
    global totals
    global letters
    global frequencies
    totals = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
    frequencies = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
    filePath = "TempDict.txt"
    f = open("TempDict.txt" , "r")
    d = f.readlines()
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
        if frequencies[l] > maxValue :
            maxIndex = l
            maxValue = frequencies[l]
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

def start() :
    global numLetters
    numLetters = eval(input("How many letters? : "))
    print("numLetters : {}\n".format(numLetters))
    if numLetters < 4 :
        print("Please enter a number >= 4.\n")
        sys.exit() 
    makeDictionary(numLetters + 2)

start()
solved = 0
while solved == 0 :
    letter = getGuess()
    print("I guess.... {}!.".format(letter))
    val = eval(input())
    while val > numLetters or val <= 0 :
        print("Please enter a valid placement\n")
        val = eval(input())

