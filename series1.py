def fact(num):
    x=1
    fact = 1
    while num > 1:
        sum = num * (num - 1)
        num = num - 2
        fact = fact * sum
        x=x+1/fact
        print(x)

num=int(input("enter the number"))
fact(num)


