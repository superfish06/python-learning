def fibonacci (n,a=0,b=1):
    for i in range(1,n+1):
        temp = a
        a=b
        b=temp+b
        print(a,b)
    return a,b

n=int(input())
fibonacci(n)





