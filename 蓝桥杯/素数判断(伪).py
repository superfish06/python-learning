import math#对于这个what求值，从2到根号what进行遍历。好处：够暴力。坏处超时

what = int (input ())
sushu = set()
for i in range(2,what+1):
    for j in range (2,int(math.sqrt(i))+1):
        if i % j ==0:
            break
    
print(sushu)