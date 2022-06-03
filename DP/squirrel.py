def squirrel(costs, possible_jumps):
    dp = [-float("inf")] * len(costs)
    dp[0] = costs[0]
    for i in range(1, len(costs)):
        for j in possible_jumps:
            if i - j >= 0:
                dp[i] = max(dp[i - j], dp[i] - costs[i]) + costs[i]

    return dp[-1]
