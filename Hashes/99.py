a = input()
s = input()

for i in range(len(a) - len(s) + 1):
    if a[i:i + len(s)] == s:
        print(i, end=" ")
