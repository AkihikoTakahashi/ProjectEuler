# coding: utf-8

# h = b ± 1 のとき.
# L^2 = h^2 + (b/2)^2
# 20L^2 = 25b^2 ± 40b + 20
# (5b ± 4)^2 - 20L^2 = -4
#
# よって, ペルの方程式 X^2 - 20Y^2 = -4 の解
# (x, y) に対して, x = 1, 4 mod 5 のとき,
# y が求める L となる.
#
# ペルの方程式 X^2 - 20Y^2 = -4 の最初の解を
# (X, Y) = (x1, y1) とすると, (x1, y1) = (4, 1)
# k 番目の解を (xk, yk)とすると, k+1 番目の解は
# (9 * xk + 40 * yk, 2 * xk + 9 * yk) となる.


def main():
    cnt_max = 12
    cnt = 0

    a, b = 4, 1
    sum_L = 0
    while cnt < cnt_max:
        if a >= 9:
            if a % 5 == 1 or a % 5 == 4:
                sum_L += b
                cnt += 1
        a, b = 9 * a + 40 * b, 2 * a + 9 * b

    return int(sum_L)


if __name__ == '__main__':
    print(main())
