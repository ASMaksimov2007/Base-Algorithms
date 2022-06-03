# Наибольшая общая подпоследовательность

def lcs(a, b):
    dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    row = len(a)
    column = len(b)

    result = []
    while column != 0 and row != 0:
        if a[row - 1] == b[column - 1]:
            result.append(b[column - 1])
            column -= 1
            row -= 1
        elif dp[row][column] == dp[row - 1][column]:
            row -= 1
        else:
            column -= 1

    return result[::-1]
