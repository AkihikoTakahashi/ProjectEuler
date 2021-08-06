# coding: utf-8

# d を p1 の桁数とすると
# s = a * 10^d + p1 = 0 mod p2 を a について解くと,
# a = -p1 * (10^d)^-1 mod p2
# a = (p2 - p1) * (10^d)^-1 mod p2
#
# a を元の式に代入すれば s が求まる.
#
# p1 の上限は 1000000 であるが, p2 の上限は 1000000 を超えるため,
# 少し多めの範囲で素数リストを作る必要がある.

from math import log10
from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def eratosthenes(n):
    '''n 以下の素数を返す'''
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes


def inv(a, p):
    return pow(a, p - 2, p)


def main():
    lim = 1000000
    primes = [i for i, p in enumerate(eratosthenes(lim + 100)) if p]
    primes = primes[2:]  # 2, 3 を除外
    sum_s = 0
    for p1, p2 in pairwise(primes):
        if p1 >= lim:
            break

        d = int(log10(p1)) + 1
        # a*10^d + p1 = 0 mod p2 を a で解く
        a = (inv(10**d, p2) * (p2 - p1)) % p2

        s = a * 10**d + p1
        sum_s += s
    return sum_s


if __name__ == '__main__':
    print(main())
