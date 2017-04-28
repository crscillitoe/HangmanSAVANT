import sys
import os

def findAllWordsWithLetterComb(letterCombination) :
    length = len(letterCombination) - 1
    listLetters = list(letterCombination)
    f = open("../Words.txt" , "r")
    d = f.readlines()
    for i in d :
        found = 0
        counter = 0
        for j in i :
            if j == listLetters[counter] and counter != length :
                counter = counter + 1
            elif j == listLetters[counter] and counter == length :
                found = 1
                break
            else :
                found = 0
                counter = 0
        if found == 1 :
            print("Found combination {} in {}".format(letterCombination , i))
    f.close()

def isAWord(word) :
    f = open("../Words.txt" , "r")
    d = f.readlines()
    for i in d :
        if i[:-1] == word :
            print("{} is a word.".format(word))
            return
    print("{} is not a word.".format(word))

while True :
    val = input()
    findAllWordsWithLetterComb(val)
    isAWord(val)
