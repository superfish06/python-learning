def fun(num,ufo):
    dps = num
    num = ufo
    ufo += dps
    print(num,ufo)
    return (num,ufo)

xuzijing = 0
zhangwenhao = 1

for i in range(0,int(input())):
    fun(xuzijing,zhangwenhao)
