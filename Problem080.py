# coding: utf-8

# 開平法を使う.
# 整数部分も2桁ごとに区切るが, 開平するのは 1 から 100 まで
# なので考慮に入れなくてよい.
#
#                  1. 4  1  4  2  ← 解
#                  -------------
#   1        |    √2.00 00 00 00
# + 1        |     1
# -----------+---------
#   24       |     1 00
# +  4       |   -   96
# -----------+---------
#   281      |        4 00
# +   1      |      - 2 81
# -----------+---------------
#   2824     |        1 19 00
# +    4     |      - 1 12 96
# -----------+------------------
#   28282    |           7 04 00
# +     2    |        -  5 69 64 ← 左の2数の乗算
# -----------+------------------
#   28284    |           2 34 36
#   ↑ 上2数の和であり, 解の2倍でもある.


def sum_digit(n, s=0):
    if n == 0:
        return s
    else:
        return sum_digit(n // 10, s + n % 10)


def square(n, max_digit, m=0):
    if max_digit == 0:
        return m
    else:
        # 解を探す.
        for i in range(9, -1, -1):
            if n - (m * 2 * 10 + i) * i > 0:
                break
        n -= (m * 2 * 10 + i) * i
        m = 10 * m + i

        return square(100 * n, max_digit - 1, m)


def main():
    max_digit = 100
    max_i = 100

    squares = [
        square(i, max_digit) for i in range(1, max_i + 1)
        if int(i**0.5)**2 != i
    ]
    return sum(sum_digit(n) for n in squares)


if __name__ == "__main__":
    print(main())
