def bubble(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def choice(array):
    for i in range(len(array) - 1):
        cur_min = float("inf")
        for j in range(i + 1, len(array)):
            if array[j] < cur_min:
                cur_min = array[j]
                cur_min_index = j
        array[i + 1], array[cur_min_index] = array[cur_min_index], array[i + 1]
    return array


def insert(array):
    for i in range(len(array) - 1):
        j = i
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1

    return array


def shit(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def count(array, bound):
    count_array = [0] * bound
    minimal_element = min(array)
    for i in range(len(array)):
        count_array[array[i] - minimal_element] += 1

    result = []
    for i in range(len(count_array)):
        result.extend([i + minimal_element] * count_array[i])

    return result


def merge_sorted_arrays(a, b):
    result = []

    while a or b:
        if not a:
            a = b[:]
            b = []

        if not b:
            result.append(a.pop())

        else:
            if a[-1] > b[-1]:
                result.append(a.pop())
            else:
                result.append(b.pop())

    return result[::-1]


def merge(array):
    # При неверной работе проверьте, что лимит на рекурсию установлен по меньшей мере в log(n) элементов
    if len(array) <= 1:
        return array

    return merge_sorted_arrays(merge(array[:len(array) // 2]), merge(array[len(array) // 2:]))


def quick(array):
    # При неверной работе проверьте, что лимит на рекурсию установлен по меньшей мере в log(n) элементов
    if len(array) <= 1:
        return array

    pivot = array[0]
    right = []
    left = []

    for i in range(1, len(array)):
        if array[i] > pivot:
            right.append(array[i])
        else:
            left.append(array[i])

    return quick(left) + [pivot] + quick(right)


def heap(array):
    pass
