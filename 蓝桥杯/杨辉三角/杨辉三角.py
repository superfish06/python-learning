N = int(input())

#做一个遍历，从第一行开始。每个数组进行运算

first = [1]
temp = [0]

while N > max(temp):
    i=1
    for j in range (i):
        if j == 0 or j == i-1:
            temp.insert[j]=first[0]#定义一下两边的数
        else:
            temp.insert[j]=first[j-1]+first[j]
        temp = first
        i +=1
print(j+1,i)