a = [10,20,30,40,50,60,70,80,90,100]
value=int(input("enter the search number"))
for i in range(0,10):
    if a[i]==value:
        print("the value found on the position %d", (i+1))
    else:
        print()
