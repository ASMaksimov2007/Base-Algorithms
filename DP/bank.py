def bank(total, values):
    children = [0] * (total + 1)
    dp = [float("inf")] * (total + 1)
    dp[0] = 0
    for value in values:
        if value <= total:
            dp[value] = 1

    for i in range(1, total + 1):
        best_parent = 0
        best_sum = float("inf")
        for j in values:
            if 0 <= i - j < total + 1 and dp[i - j] < best_sum:
                best_sum = dp[i - j]
                best_parent = i - j
        dp[i] = best_sum + 1
        children[i] = best_parent

    result = []

    if dp[total] == float("inf"):
        return False

    # Восстановление ответа
    x = total
    while x != 0:
        result.append(x - children[x])
        x = children[x]
    return result
