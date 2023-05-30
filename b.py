list=[]
list1=[]
list2=[]
number=int(input("Enter the number"))
for i in range(1,number+1):
    if number%i==0:
        list.append(i)
print(list)
for i in range(2,len(list)):
    a=int(int(list[i])**0.5)
    list1.append(a)
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

print("the numbers are",list2)
print("total numbers are",len(list2))
