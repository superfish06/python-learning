import math


def extended_gcd(a, b):
    """扩展欧几里得算法，返回 (gcd(a, b), x, y)"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def merge_congruences(a1, m1, a2, m2):
    """合并两个同余方程"""
    gcd, x, y = extended_gcd(m1, m2)
    if (a2 - a1) % gcd != 0:
        raise ValueError("无解：模数不满足合并条件")

    # 计算合并后的模数和余数
    new_m = m1 * m2 // gcd
    new_a = (a1 + x * (a2 - a1) // gcd * m1) % new_m
    return new_a, new_m


def result(a_list, m_list):
    """求解同余方程组（支持非两两互质的模数）"""
    # 初始化第一个同余方程
    a, m = a_list[0], m_list[0]

    # 逐个合并同余方程
    for i in range(1, len(a_list)):
        a, m = merge_congruences(a, m, a_list[i], m_list[i])

    return a


if __name__ == '__main__':
    print("请输入余数 a_i，以逗号分隔：")
    a_list = list(map(int, input().split(",")))
    print("请输入模数 m_i，以逗号分隔：")
    m_list = list(map(int, input().split(",")))

    try:
        result_value = result(a_list, m_list)
        print("最终结果为：")
        print(result_value)
    except ValueError as e:
        print(e)
