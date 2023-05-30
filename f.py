list=[]
r=int(input("enter the range of nymber="))
for i in range(0,r):
    a=int(input("enter the number="))
    list.append(a)
b=max(list)
for i in range(0,r):
    if b==list[i]:
        x=i
print("very tough ")

