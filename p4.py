def pow(p,n):
    if n==0:
        return 1
    else:
        return p*pow(p,n-1)
p=int(input("enter the number"))
n=int(input("enter the power"))

ans=pow(p,n)
print(ans)
