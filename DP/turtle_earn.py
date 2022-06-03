def turtle_earn(field):
    n = len(field)
    m = len(field[0])

    dp = [[-float("inf")] * (m + 1) for i in range(n + 1)]

    dp[1][1] = field[0][0]

    for i in range(n):
        for j in range(m):
            if dp[i + 1][j + 1] == -float("inf"):
                dp[i + 1][j + 1] = max(dp[i][j + 1],
                                       dp[i + 1][j]) + field[i][j]

    return dp[n][m]
