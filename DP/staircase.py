def staircase(costs, jump_range):
    dp = [float("inf")] * len(costs)
    dp[0] = costs[0]
    for i in range(1, len(costs)):
        for j in range(1, jump_range + 1):
            if i - j >= 0:
                dp[i] = min(dp[i - j], dp[i] - costs[i]) + costs[i]

    return dp[-1]
