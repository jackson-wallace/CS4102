


def logCutting(prices, n):

    dp = [0 for _ in range(len(prices))]
    
    dp[0] = 0
    choices = []

    for i in range(len(prices)):
        best = 0
        for j in range(i+1):
            best = max(best, dp[i-j]+prices[j])
            choices[i] = j
        dp[i] = best
    print(dp)
    print(choices)
    return dp[n]



prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 7

print(logCutting(prices, n))