def lcstring(a, b):
    dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    maximum_x = 0
    maximum_y = 0
    maximum_len = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] >= maximum_len:
                    maximum_x = i - 1
                    maximum_y = j - 1
                    maximum_len = dp[i][j]

    return a[maximum_x - maximum_len + 1:maximum_x + 1]
