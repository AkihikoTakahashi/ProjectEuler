# coding: utf-8

# ピタゴラス数(a, b, c) に対して
# b - a = 0 mod c となるものを数える.
#
# d = b - a とすると, c = nd
# a^2 + b^2 = c^2
# 2a^2 + 2ad + d^2 = n^2 * d^2
# 2a^2 / d^2 + 4a / d - 2n^2 = -2
# (2a / d + 1)^2 - 2n^2 = -1
#
# よってペルの方程式 X^2 - 2Y^2 = -1 の自明でない最小解は
# (X, Y) = (1, 1)
# 解の漸化式は (x_k+1, y_k+1) = (3x_k + 4y_k, 2x_k + 3y_k)
# また, x_k+1 は常に奇数であるので, (2a / d +1) の形を満す.
#
# ペルの方程式の解 (x, y) とすると,
# 2a / d + 1 = x, n = y
# 2a = dx - d
# 三角形の辺の和は
# a + b + c = a + (a + d) + nd = 2a + d + yd
# = dx + yd = d(x + y)
# よって解の組 (x, y) に対し, 100000000 / (x + y) 個,
# 条件を満す直角三角形が存在する.


def main():
    lim = 100000000
    cnt = 0

    x, y = 1, 1
    while x + y < lim:
        if x >= 3:
            cnt += int(lim / (x + y))
        x, y = 3 * x + 4 * y, 2 * x + 3 * y

    return cnt


if __name__ == '__main__':
    print(main())
