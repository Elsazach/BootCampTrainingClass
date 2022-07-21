def cal(a,b,c):
    if(a=='+'):
        print(b+c)
    elif(a=='-'):
        print(b-c)
    elif(a=='*'):
        print(b*c)
    elif(a=='/' and c!=0):
        print(b/c)
    else:
        print("invalid");
a=input("Enter which operation to be performed")
b=int(input("enter first number"))
c=int(input("enter second number"))
cal(a,b,c)
    
