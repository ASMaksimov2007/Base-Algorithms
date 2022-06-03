# Время работы - O(N * N)

def lis_slow(array):
    dp = [1] * len(array)

    for i in range(len(array)):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    lis_len = max(dp)
    prev = None
    pointer = dp.index(lis_len)

    result = [array[pointer]]
    while pointer != 0:
        for i in range(pointer - 1, -1, -1):
            if dp[i] + 1 == dp[pointer]:
                result.append(array[i])
                pointer = i
                break

    return result[::-1]


# Время работы - O(N log N)

def lis_fast(array):
    n = len(array)
    dp = [float("inf")] * n
    pos = [0] * n
    prev = [0] * n
    most_right = 0
    pos[0] = -1
    dp[0] = -float("inf")
    for i in range(n):
        j = bisect.bisect_left(dp, array[i])
        if j >= len(dp):
            j = len(dp) - 1
        if j == 0:
            j = 1
        if dp[j - 1] < array[i] < dp[j]:
            dp[j] = array[i]
            pos[j] = i
            prev[i] = pos[j - 1]
            most_right = max(most_right, j)

    # Восстановление ответа
    answer = list()
    p = pos[most_right]
    while p != -1:
        answer.append(array[p])
        p = prev[p]

    return answer[::-1]
