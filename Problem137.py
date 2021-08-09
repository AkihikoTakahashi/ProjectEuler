# coding: utf-8

# Ar(x) = x * F1 + x^2 * F2 + x^3 * F3 + ...
# xAr(x) =         x^2 * F1 + x^3 * F2 + ...
# x^2Ar(x) =                  x^3 * F1 + ...
#
# それぞれ引き算すると
# (1 - x - x^2)Ar(x) = x * F1 + (F2 - F1)x^2 + (F3 - F2 - F1)x^3 + ...
# (1 - x - x^2)Ar(x) = x
#
# Ar(x) は整数より Ar(x) = n とおいて
# (1 - x - x^2)n = x
# nx^2 + (n+1)x - n = 0
# x は有理数なので, 2次方程式は有理数解を持つ.
# よって判別式 D は平方数.
#
# D = (n+1)^2 + 4n^2 = 5n^2 + 2n + 1 = m^2 とする.
# 5n^2 + 2n - m^2 = -1 を変形すると
# (5n + 1)^2 - 5m^2 = -4
#
# ペルの方程式 X^2 - 5Y^2 = -4 の最小解を (a_1, b_1) とすると
# a_1 = 1, b_1 = 1
# 方程式の解は (a_n+1, b_n+1) = ((3a_n + 5b_n)/2, (a_n, 3b_n)/2)
# と書ける.
# https://ja.wikipedia.org/wiki/%E3%83%9A%E3%83%AB%E6%96%B9%E7%A8%8B%E5%BC%8F
#
# よってペルの方程式の解 a_k に対し, a_k = 1 mod 5 であれば,
# n = (a_k - 1)/5
# が導ける.


def main():
    cnt_max = 15
    cnt = 0

    # a^2 - 5b^2 = -4 の最初の解は (a, b) = (1, 1)
    a, b = 1, 1

    while cnt < cnt_max:
        if a >= 6 and a % 5 == 1:
            n = (a - 1) // 5
            cnt += 1
        a, b = (3 * a + 5 * b) // 2, (a + 3 * b) // 2

    return n


if __name__ == '__main__':
    print(main())
