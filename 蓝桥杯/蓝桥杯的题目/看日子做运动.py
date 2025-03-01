months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

hz=[13,1,2,3,5,4,4,2,2,2]

def leap_year(year):
    return year % 400 ==0 or (year %4 == 0 and year %100 != 0)

def solve ():
    ans = 0
    for year in range (2000,2025):
        months[2]=29 if leap_year(year) else 28
        for month in range(1,13):
            for day in range (1,months[month]+1):
                cnt = 0
                y1,y2,y3,y4 = year //1000,year//100%10,year//10%10,year % 10
                m1,m2 = month // 10,month%10
                d1,d2 = day // 10 ,day % 10
                cnt += hz[y1]+hz[y2]+hz[y3]+hz[y4]\
                        +hz[m1]+hz[m2]+hz[d1]+hz[d2]
                if cnt > 50:
                    ans += 1

                if year == 2024 and month == 4 and day == 13 :
                    print (ans)
                    return


solve()