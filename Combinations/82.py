def gen_binary(size, k, ans, curr):
    if len(curr) == size:
        print(curr)
        return
    for i in range(k):
        gen_binary(size, k, ans, curr + str(i))
    return


n, k = map(int, input().split())
gen_binary(n, k, [], "")
