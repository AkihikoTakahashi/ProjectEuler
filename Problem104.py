# coding: utf-8

from math import log10


def is_pandigit(n):
    d = 0
    c = 0
    tmp = 0

    while n > 0:
        tmp = d
        d = d | 1 << ((n % 10 - 1) % 32)
        if d == tmp:
            return False
        n //= 10
        c += 1
    return d == (1 << c) - 1


def gen_fibo():
    a = 1
    b = 0
    while True:
        yield a
        a, b = a + b, a


def main():
    for i, n in enumerate(gen_fibo(), start=1):
        if n < 10**10:
            continue

        e = n % 10**9
        s = n // 10 ** (int(log10(n) + 1) - 9)
        if is_pandigit(e) and is_pandigit(s):
            return i


if __name__ == '__main__':
    print(main())
