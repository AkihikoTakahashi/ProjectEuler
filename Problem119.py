# coding: utf-8

# N桁の数が n = a ^ e と書けるなら, a の取り得る範囲は
# 2 <= a <= 9N
# である.
#
# 2 ^ e <= n < 10 ^ N         (n は 2^e 以上であり, かつ, N桁の数)
# 10 ^ (N-1) < n <= (9N) ^ e  (n は (9N)^e 以下であり, かつ, N桁の数)
#
# よって
# elog2 < Nlog10  ==>  e < Nlog10 / log2
# (N-1)log10 < elog(9N)  ==>  e > (N-1)log10/log(9N)
#
# ゆえに e の取り得る範囲は
# (N-1)log10 / log(9N) < e < Nlog10 / log2
# となる.

from math import log
from itertools import count


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def range_e(digit):
    return range(
        int((digit - 1) * log(10) / log(9 * digit)) + 1,
        int(digit * log(10) / log(2)))


# a を e 乗して d 桁になる最小の a
# 10^(d-1) = a^e  ==>  10^((d-1)/e) = a
def first_pow(digit, e):
    a = int(10**((digit - 1) / e))
    while a**e < 10**(digit - 1):
        a += 1
    return a


def find_digit_pow_sum(d):

    digit_pow_sum_d = []
    for e in range_e(d):
        begin = first_pow(d, e)
        end = first_pow(d + 1, e)

        for n in range(begin, end):
            if n == digit_sum(n**e):
                digit_pow_sum_d.append(n**e)
    return sorted(digit_pow_sum_d)


def main():
    N = 30
    digit_pow_sums = []

    for d in count(2):
        digit_pow_sums += find_digit_pow_sum(d)
        if len(digit_pow_sums) >= N:
            break
    return digit_pow_sums[N - 1]


if __name__ == '__main__':
    print(main())
