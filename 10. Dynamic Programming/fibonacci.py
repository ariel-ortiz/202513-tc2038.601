def fibo_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_dp(n: int) -> int:
    if n == 0:
        return 0
    dp: list[int] = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    print(fibo_recursive(7))
    # print(fibo_recursive(40))
    print(fibo_dp(7))
    print(fibo_dp(1000))
