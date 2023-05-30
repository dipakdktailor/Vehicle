def fib(num):
    a = 0
    b = 1
    sum=0
    print (a,"\t",b,end="\t")
    while num>sum:
        sum = a+b

        a=b
        b=sum
        print(sum, end="\t")


num=int(input("enter the number"))
fib(num)

