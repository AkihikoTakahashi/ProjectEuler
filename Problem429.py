# coding: utf-8

# n = p1^e1 * p2^e2 のとき,
# S(n!) = (1 + (p1^e1)^2)(1 + (p2^e2))
# と書けることから, n! が n 以下の素数で何度割れるか数える.
#
# n! が p で割れる回数は n//p + n//p^2 + n//p^3 + ... で求まる.

from math import log


def eratosthenes(n):
    ''' Returns  a list of primes < n '''
    primes = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            primes[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if primes[i]]


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
