letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' ,
            'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' ,
            'u' , 'v' , 'w' , 'x' , 'y' , 'z' , '\n']
filePath = input("Enter the file path : ")
f = open(filePath, "r+")
d = f.readlines()
f.seek(0)
for i in d :
    for c in i :
        found = 0
        for a in letters :
            if a == c :
                found = 1
                break
        if found == 0 :
            break
    if found == 1 :
        f.write(i)
f.truncate()
f.close()
