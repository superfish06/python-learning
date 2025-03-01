n = int(input())

Flag=[True for i in range(n+1)]
for i in range(2, int(n**(0.5))+1):
    if Flag[i] :
        tmp = i+i
        while tmp < n+1:
            Flag [tmp]=False
            tmp +=i
sum = 0
for i in range(2,n+1):
    if n % i==0 and Flag[i] :
        sum += 1
print(sum)# 输入 n
