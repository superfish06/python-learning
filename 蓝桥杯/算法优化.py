def fast_pow (a,b, mod):
    res = 1
    while b >0:
        if b % 2== 1:
            res = res*a%mod
        a = a*a % mod
        b = b //2
    return res

fast_pow(3,5,4)