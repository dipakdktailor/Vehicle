x=int(input("enter the range of array"))
a=[int(input("Enter the number for array"))for i in range(x)]
b=int(input("Enter the number that you want to print"))
for i in range(0,x):
    for j in range(0,x-1-i):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
for k in range(0,b):
    print(a[k])
