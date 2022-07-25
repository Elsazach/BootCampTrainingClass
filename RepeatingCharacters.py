print("Enter a String: ")
str = input()
strlist = []
strlist=list(str)
newlist = []
j = 0
for i in range(len(strlist)):
    if str[i] not in newlist:
        newlist.insert(j, str[i])
        j = j+1

str = ""
str = str.join(newlist)
print(str)


        
