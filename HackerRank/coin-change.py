# URL: https://www.hackerrank.com/challenges/coin-change/problem

def getWays(n, coins):
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]


n, m = map(int, input().split())
coins = list(map(int, input().split()))


result = getWays(n, coins)
print(result)