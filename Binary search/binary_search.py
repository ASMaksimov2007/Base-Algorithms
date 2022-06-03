def check(n):
    # функция проверки - БП по ответу
    return n < 10


l = 0
r = 101  # ставим границу в n + 1

while r - l > 1:
    mid = (r + l) // 2

    if check(mid):
        l = mid
    else:
        r = mid

# Где ответ - в L или R?
