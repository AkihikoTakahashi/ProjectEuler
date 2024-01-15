# coding: utf-8

from functools import lru_cache
from math import isqrt


def eratosthenes(n):
    """Returns a list of primes less than n."""

    primes = [False, False] + [True] * (n - 2)
    primes[4::2] = [False] * ((n + 1) // 2 - 2)
    for i in range(3, isqrt(n) + 1, 2):
        if primes[i]:
            primes[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    primes = [i for i, p in enumerate(primes) if p]
    return primes


@lru_cache(maxsize=None)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, isqrt(n) + 1, 2))


def is_catPrime(p1, p2):
    return is_prime(int(str(p1) + str(p2))) and is_prime(
        int(str(p2) + str(p1))
    )


def is_all_catPrime(p, primes):
    return all(is_catPrime(p, p1) for p1 in primes)


# found はすでに prime pair set な素数のリスト
# cand_primes は max(found) なる素数のリスト
def find_new_pair(found, cand_primes):
    cands = []
    for p1 in found:
        for p2 in cand_primes:
            if is_catPrime(p1, p2):
                cands.append(found + [p2])
    return cands


def find(found, cand_primes, cnt=5):
    if len(found) == cnt:
        return found

    new_found = found
    for i in range(len(cand_primes)):
        p = cand_primes[i]
        if is_all_catPrime(p, found):
            new_found = find(found + [p], cand_primes[i + 1 :], cnt)
            if len(new_found) > 0:
                return new_found
    return []


def main():
    lim = 10**4
    primes = eratosthenes(lim)
    N = 5

    # 明らかに p = 2, p = 5 は使わない
    del primes[0]
    del primes[1]

    for i in range(len(primes)):
        prime5 = find([primes[i]], primes[i + 1 :], N)
        if len(prime5) == N:
            print(prime5, sum(prime5))
            # print(sum(prime5))


if __name__ == '__main__':
    print(main())
