nums=input()
cnt = 0

def check(num):
    zifu = str(num)#先召唤一个字符串
    woc=len(zifu)
    for weizhi in range (woc):#再来一个循环，所求的是从索引0到索引最大奇偶
        if (weizhi % 2 == 0 and int(zifu[weizhi]) % 2 ==0) or (weizhi %2 != 0 and int(zifu[weizhi]) % 2 != 0):
                return False
    return True

for i in range(1,int(nums)+1):
    check(i)
    if check(i) == True:
        cnt = cnt+1

print (cnt)
