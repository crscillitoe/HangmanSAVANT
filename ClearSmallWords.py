filePath = input("Enter the file path : ")
f = open(filePath , "r+")
d = f.readlines()
f.seek(0)
for i in d :
    if len(i) >= 5 : 
        f.write(i)
f.truncate()
f.close()
