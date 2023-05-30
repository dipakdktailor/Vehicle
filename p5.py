def mul(a,b):
    if b >=1:
        return a + mul(a, b - 1)
    else:
        return 0

a=int(input("enter the first number"))
b=int(input("enter the second number"))


ans=mul(a,b)
print("a*b=",ans)