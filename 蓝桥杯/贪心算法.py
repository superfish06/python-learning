def coin_change(amount):
    coin_denominations = [25,10,5,1]
    coin_count =  0
    while amount > 0:
        for i in range(len(coin_denominations)):
            coin_count += amount // coin_denominations[i]
            amount= amount % coin_denominations[i]
            if amount == 0:
                break
    return coin_count
amount = 63
result = coin_change(amount)
print(f'{amount} {result}')
