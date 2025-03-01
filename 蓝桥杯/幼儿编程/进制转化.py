import os
import sys

n = int(input())
letters = [chr(i) for i in range(65, 91)]  # 从'A'到'Z'的字母列表
dps = ""
while n > 0:
    n -= 1  # 先减1以正确处理余数
    remainder = n % 26  # 计算余数
    dps = letters[remainder] + dps  # 将当前字母添加到结果的前面
    n = n // 26  # 更新n为商数进行下一轮循环
print(dps)