# coding: utf-8

# 2^j が 123 で始まる 678910 番目の j を求める.
#
# N = 2^j  ==>  log10(N) = jlog10(2) より, k < jlog10(2) < k+1 とすると, N は k 桁である.
# よって N = 10^k * 10^(jlog10(2) - k) である.
# 10^k は先頭の数値に影響しないので, 10^(jlog10(2) - k) の先頭 3 文字が 123 であるか判定する.

from math import log10
from itertools import count, islice


def gen_p(L):
    len_L = int(log10(L)) + 1
    for j in count(1):
        d = log10(2) * j
        int_d = int(d)

        if L < 10**(d - int_d) * 10**(len_L - 1) < L + 1:
            yield j


def nth(iterable, n):
    return next(islice(iterable, n, None))


def main():
    L = 123
    n = 678910

    return nth(gen_p(L), n - 1)


if __name__ == '__main__':
    print(main())
