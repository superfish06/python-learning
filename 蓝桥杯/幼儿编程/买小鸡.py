cnt = 0
for rooster in range(0,21):
    for hen in range (0,34):
        if 5 * rooster + 3 * hen <= 100 and 3*(100-5*rooster-3*hen) + rooster + hen == 100:
            print(rooster,hen,3*(100-5*rooster-3*hen))
            cnt = cnt+1
        else:
            continue
print(cnt)