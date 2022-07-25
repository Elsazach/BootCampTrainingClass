print("enter th string?")
count=0
str1=input()
print("enter the character ?")
ch=input()
for i in str1:
    if(str1.count(i)>=1):
        str2=str1.replace(i,"")
print(str2)
