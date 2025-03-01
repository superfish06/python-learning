correct_password = input()
n = 0
for digit1 in range(0,10):
    for digit2 in range(0,10):
        for digit3 in range(0,10):
            for digit4 in range(0,10):
                m = str(digit1*1000+digit2*100+digit3*10+digit4)
                if m == correct_password :
                    print (m)
                    break
                else :
                    n = n + 1
                    continue
print (n)