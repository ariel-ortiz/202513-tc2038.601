def coin_change(coins: list[int], ammount: int) -> list[int] | None:
    omega: list[int] = [0] * (ammount + 1)
    dp: list[list[int]] = [omega] * (ammount + 1)
    dp[0] = []
    for i in range(1, ammount + 1):
        for coin in coins:
            if i >= coin:
                candidate: list[int] = dp[i - coin] + [coin]
                if len(candidate) < len(dp[i]):
                    dp[i] = candidate
    if dp[ammount] is omega:
        return None
    return sorted(dp[ammount], reverse=True)


if __name__ == "__main__":
    for i in range(101):
        print(i, coin_change([2, 5, 10, 20], i))
