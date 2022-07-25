list1 = []
n = int(input("enter size of array : "))
print("enter array elements")
for i in range(0,n,1):
    p=int(input())
    list1.append(p)
lar = list1[0]
small = list1[0]
for i in range(0,n,1):
    if list1[i]>lar:
        lar = list1[i]
    if list1[i]<small:
        small = list1[i]
        
print("largest element ",lar)
print("smallest element ",small)
