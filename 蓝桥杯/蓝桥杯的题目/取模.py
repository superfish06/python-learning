def mod_power(base, exponent, mod):
    result = 1
    base = base % mod  # 先对 base 取模
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2
    return result


result = mod_power(base, exponent, mod)
print(f"最终结果：{base}^{exponent} mod {mod} = {result}")