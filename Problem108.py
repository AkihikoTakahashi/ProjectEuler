# coding: utf-8

# 1/x + 1/y = 1/n
#
# n = 4 なら
# 1/5 + 1/20 = 1/4
# 1/6 + 1/12 = 1/4
# 1/8 + 1/8 = 1/4
# の3つ
#
# 1/x + 1/y = 1/n <=> yn + xn = xy
# x(y-n) = yn
# x = yn / (y-n)
#
# x: 自然数 より yn / (y-n) も自然数
#
# n = 4 なら
# x = 4y /(y-4)
# (y=5, x=20), (y=6, x=12), (y=8, x=8)
# の3つが求まる.
#

max_cnt = 1000

n = 3
while True:
    cnt = 0
    y = n + 1
    while y <= 2 * n:
        if n * y % (y - n) == 0:
            print(n * y // (y - n), y, n)
            cnt += 1
        y += 1

    n += 1
    if cnt >= max_cnt:
        break
print(n - 1)
