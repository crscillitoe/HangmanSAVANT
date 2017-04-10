letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' ,
            'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' ,
            'u' , 'v' , 'w' , 'x' , 'y' , 'z' , '\n']
totals = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
filePath = input("Enter the file path : ")
f = open(filePath, "r+")
d = f.readlines()
f.seek(0)
for i in d :
    for c in i :
        if c != '\n' :
            for l in range(26) :
                if letters[l] == c :
                    totals[l] = totals[l] + 1
frequencies = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0]
total = 0
for l in range(26) :
    total = total + totals[l]
for l in range(26) :
    frequencies[l] = totals[l]/total
    print("Letter : {}\n Frequency : {}\n".format(letters[l] , frequencies[l]))
totalFreq = 0
for l in range(26) :
    totalFreq = totalFreq + frequencies[l]
print("Frequencies added up : {}\n".format(totalFreq))
