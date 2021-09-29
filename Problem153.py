# coding: utf-8

from math import gcd
from itertools import takewhile, count


def is_squre(n):
    return int(n**0.5)**2 == n


def main():
    lim = 10**8
    s = 0

    for i in range(1, lim + 1):
        s += (lim // i) * i  # 整数の和

    for a in range(1, int(lim**0.5) + 1):
        for b in range(1, a + 1):
            if gcd(a, b) == 1:
                n = a**2 + b**2
                val = 2 * (a + b) if a != b else a + b
                for k in takewhile(lambda k: n * k <= lim, count(1)):
                    s += k * val * (lim // (n * k))
    return s


if __name__ == '__main__':
    print(main())
