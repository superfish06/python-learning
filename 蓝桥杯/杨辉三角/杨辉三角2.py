def print_pascals_triangle(n):
    triangle = []  # 用于存储杨辉三角的每一行

    for i in range(n):
        row = [1] * (i + 1)  # 创建当前行，初始值全部为1
        if i > 1:  # 从第3行开始，需要计算中间的值
            for j in range(1, i):#写一个遍历，不用切片也可以，
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]#上一行两个玩意相加
        triangle.append(row)  # 将当前行添加到杨辉三角中

    # 打印杨辉三角
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 4))  # 使用center方法居中显示


# 示例：输出前5行杨辉三角
print_pascals_triangle(8)
