S=int(input("Enter the number of seats ="))
N=int(input("Enter the Size of contigent ="))
k=int(input("Enter the Size of contigent who willingly sit on wet chairs ="))
M=int(input("Enter the Size of Blocks ="))
list=[]
for i in range(0,M):
    a=int(input("enter the blocks"))
    list.append(a)
b=max(list)
list.remove(b)
c=max(list)
for i in range(0,M):
    if b<=list[i]:
        a=a+list[i]
    else:
        d=a+b
        a=a+d
print(a)




