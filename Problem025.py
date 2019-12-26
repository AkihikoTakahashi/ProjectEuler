# coding: utf-8

from itertools import count, dropwhile
from math import log10


def gen_fibo():
    n0 = 0
    n1 = 1

    while True:
        yield n1
        n0, n1 = n1, n0 + n1


def main():
    L = 1000
    next(dropwhile(lambda x: log10(x[0]) < L, zip(gen_fibo(), count(1))))[1]


if __name__ == "__main__":
    print(main())
