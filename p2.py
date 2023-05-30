num=int(input("enter the number"))
i=0
rev = 0
h=0
print(" ")
print(rev)
while rev!=0:
    d=rev%10
    rev=rev//10
    i+=1
    if d==1:
        print("one")
    elif d==2:
        print("two")
    elif d==3:
        print("three")
    elif d==4:
        print("four")
    elif d==5:
        print("five")
    elif d==6:
        print("six")
    elif d==7:
        print("seven")
    elif d==8:
        print("eight")
    elif d==9:
        print("nine")
    elif d==0:
        print("zero")
    else:
        print("error")





