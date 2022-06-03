def backpack(max_weight, weights, costs):
    if len(weights) != len(costs):
        raise ValueError("weights and costs length must be equal")

    dp = [[0] * (max_weight + 1) for i in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(1, max_weight + 1):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1]
                               [j - weights[i - 1]] + costs[i - 1])

    # Восстановление ответа
    result = []

    i = len(weights)
    j = max_weight

    while dp[i][j] > 0 and i > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            i -= 1
            j -= weights[i]
            result.append((i + 1, weights[i], costs[i]))

    return result[::-1]
