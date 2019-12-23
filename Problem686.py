# coding: utf-8

# 2^j が 123 で始まる 678910 番目の j を求める.
#
# N = 2^j  ==>  log10(N) = jlog10(2) より, k < jlog10(2) < k+1 とすると, N は k 桁である.
# よって N = 10^k * 10^(jlog10(2) - k) である.
# 10^k は先頭の数値に影響しないので, 10^(jlog10(2) - k) の先頭が L か判定する.

from math import log10
from itertools import count, islice


def gen_p(L):
    d_L = int(log10(L)) + 1
    log10_L = log10(L)
    log10_L1 = log10(L + 1)

    log10_2 = log10(2)
    d = 0
    for j in count(1):
        d += log10_2
        int_d = int(d)

        # L < 10**(d - int_d + d_L - 1) < L + 1 ==>
        # log10(L) < d - int_d + d_L - 1 < log10(L + 1)
        if log10_L < d - int_d + d_L - 1 < log10_L1:
            yield j


def main():
    L = 123
    n = 678910

    return next(islice(gen_p(L), n - 1, None))


if __name__ == '__main__':
    print(main())
