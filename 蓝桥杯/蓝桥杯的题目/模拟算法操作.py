num = int (input())
time = int (input())

def function (x,m):
    while m != 0 and x != 0:
        if x%2 != 0:
            x = 3*x+1

        else :
            x = x/2

        m -= 1
    return x,m

num, time = function(num, time)

print (num, time)