print("enter the string?")
str1=input()
str2=""
print(str1)
for i in range(len(str1)-1,-1,-1):
    str2=str2+str1[i]
if(str1==str2):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
