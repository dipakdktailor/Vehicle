num=int(input("enter the number"))
fact=1
while num>1:
    sum=num*(num-1)
    num=num-2
    fact=fact*sum

print(fact)
