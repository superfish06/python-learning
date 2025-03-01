from functools import reduce

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}#合成数
    return digits[s]

def fn(x, y):
    return x * 10 + y


m=reduce(fn, map(char2num, '13579'))

print(m)