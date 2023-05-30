def rev(num):
    if num>0:
        return num%10
        num=num//10
    else :
        return num

num=int(input("enter the number"))
ans=rev(num)
print(ans)


