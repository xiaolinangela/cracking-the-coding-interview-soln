def coins_change(coins, amount):
    table = [float('inf') for x in range(amount+1)]
    table[0] = 0
    for i in range(1, amount+1):
        if i in coins:
            table[i] = 1
        else:
            temp = [float('inf')] * len(coins)
            for j in range(len(coins)):
                if i > coins[j]:
                    temp[j] = 1 + table[i-coins[j]]
            table[i] = min(temp)

    return table[amount] if table[amount] != float('inf') else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coins_change(coins, amount))
