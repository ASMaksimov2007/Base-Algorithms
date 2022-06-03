import bisect


def binary_search(array, element):
    """Ищем индекс первого элемента, большего или равного element."""
    l = -1
    r = len(array)
    while r - l > 1:
        mid = (r + l) // 2
        if array[mid] < element:
            l = mid
        else:
            r = mid
    return r


def lis(array):
    n = len(array)
    dp = [float("inf")] * n
    pos = [0] * n
    prev = [0] * n
    most_right = 0
    pos[0] = -1
    dp[0] = -float("inf")
    for i in range(n):
        j = binary_search(dp, array[i])
        if j >= len(dp):
            j = len(dp) - 1
        if j == 0:
            j = 1
        if dp[j - 1] < array[i] < dp[j]:
            dp[j] = array[i]
            pos[j] = i
            prev[i] = pos[j - 1]
            most_right = max(most_right, j)

    answer = list()
    p = pos[most_right]
    while p != -1:
        answer.append(array[p])
        p = prev[p]

    return answer[::-1]


def quadratic_lis_length(array):
    n = len(array)
    dp = [1] * n

    for i in range(n):
        curr_max = 0
        for j in range(i - 1, -1, -1):
            if array[i] > array[j] and dp[j] > curr_max:
                curr_max = dp[j]
        dp[i] = curr_max + 1

    answer = max(dp)
    return answer
