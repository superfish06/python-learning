def hanoi(n, a, b, c):
   hanoi(n-1, a, c, b)
   print(b,c)#规定数组转换方向
   c.append(a.pop())
   print(b,c)
   hanoi(n-1, b, a, c)
   print(b,c)

a = list(range(1,65))
b = []
c = []
n=int(input())
hanoi(n,a,b,c)
print(a,b,c)