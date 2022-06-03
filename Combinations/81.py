def gen_binary(l, ans, curr):
    if len(curr) >= l:
        print(curr)
        return
    for i in range(1, -1, -1):
        gen_binary(l, ans, curr + str(i))
    return ans


n = int(input())
gen_binary(n, [], "")
