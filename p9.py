def hcf(a,b,i):
    if i==0:
        if a<b:
            i=a
        else:
            i=b
    if i>=2:
        if a%i==0 and b%i==0:
            return i
        else:
            return hcf(a,b,i-1)
    else:
        return i

a=int(input("enter the 1st number"))
b=int(input("enter the second number"))
ans=hcf(a,b,0)
print(ans)



