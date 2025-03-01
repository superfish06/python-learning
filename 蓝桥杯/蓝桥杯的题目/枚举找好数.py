fanwei = int (input())
cnt = 0

def check_number(num,cnt):

    # 将数字转换为字符串，方便逐位处理
    num_str = str(num)
    length = len(num_str)

    for i in range(length):  # 从左往右遍历每一位
        digit = int(num_str[i])  # 获取当前位的数字 检查奇数位和偶数位
        if (i + 1) % 2 == 1:  # 奇数位
            if digit % 2 != 1:  # 奇数位必须是奇数
                return False
        else:  # 偶数位
            if digit % 2 != 0:  # 偶数位必须是偶数
                return False
    return True
2
for num in range (1,fanwei + 1):
    if check_number(num,cnt):
        cnt +=1

print(cnt)
