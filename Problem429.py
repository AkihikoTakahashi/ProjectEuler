# coding: utf-8

# n = p1^e1 * p2^e2 のとき,
# S(n!) = (1 + (p1^e1)^2)(1 + (p2^e2))
# と書けることから, n! が n 以下の素数で何度割れるか数える.
#
# n! が p で割れる回数は n//p + n//p^2 + n//p^3 + ... で求まる.

from math import log


def eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]


def main():
    N = 10**8
    M = 1000000009

    primes = eratosthenes(N)
    s = 1
    for p in primes:
        e = 0
        max_e = int(log(N, p))
        for _e in range(1, max_e + 1):
            e += N // p**_e
        s = (s * (1 + pow(p, 2 * e, M))) % M
    return s


if __name__ == '__main__':
    print(main())
