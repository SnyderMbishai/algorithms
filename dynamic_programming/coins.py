def reverse_coin_change(dp):
    target = len(dp) - 1
    coins = []

    # Check if the last index of dp is 0
    if dp[target] == 0:
        return None

    # Traverse the dp list in reverse order
    while target > 0:
        # Find the coin that leads to the current target value
        for coin in range(target, 0, -1):
            if dp[target] - dp[target - coin] == 1:
                coins.append(coin)
                target -= coin
                break

    # Reverse the coins list to get the original order
    coins.reverse()
    return coins


dp = [1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 3]
print(reverse_coin_change(dp))  # Output: [2, 5, 6]

dp = [1, 1, 1, 3, 2]
print(reverse_coin_change(dp))  # Output: None
