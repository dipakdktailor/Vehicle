decimal=int(input("enter the number"))
i=0
n=1
bin=0
while decimal > 0:
    d=decimal%2
    bin=n*d+bin
    n=n*10
    decimal=decimal//2
    i+=1
print(bin)

i=0
n=1
octt=0
while decimal > 0:
    d=decimal%8
    octt=n*d+octt
    n=n*10
    decimal=decimal//8
    i+=1
print(octt)

'''hex=""
while decimal > 0:
    d=decimal%16
    if d==10:
        s="A"
    elif d==11:
        s="B"
    elif d==12:
        s="C" 
    elif d==13:
        s="D"
    elif d==14:
        s="E"
    elif
        
    n=n*10
    decimal=decimal//16
    i+=1
print(hexx,end=" ")'''


S