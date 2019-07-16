# coding: utf-8

from math import log10
from itertools import count


def gen_fibo():
    n0 = 0
    n1 = 1

    while True:
        yield n1
        n0, n1 = n1, n0 + n1


def main():
    fibo = gen_fibo()
    digit_lim = 1000
    for i in count(1):
        n = next(fibo)
        if log10(n) - 1 > digit_lim:
            return i


if __name__ == "__main__":
    print(main())
