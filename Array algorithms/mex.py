def mex(array):
    """
    Time complexity: O(N)
    Memory complexity: O(2N) in the worst case
    """

    items = set(array)
    for i in range(len(array)):
        if i not in items:
            return i
    return len(array)


print(mex([0, 5, 1, 2, 3, 4]))
