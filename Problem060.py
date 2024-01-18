# coding: utf-8

from math import isqrt


def eratosthenes(n, ret_num=True):
    """Returns a list of primes less than n."""

    primes = [False, False] + [True] * (n - 2)
    primes[4::2] = [False] * ((n + 1) // 2 - 2)
    for i in range(3, isqrt(n) + 1, 2):
        if primes[i]:
            primes[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    if ret_num:
        return [i for i, p in enumerate(primes) if p]
    else:
        return primes


def find(lim, cnt=5):
    # p1 と p2 を連結しても素数か判定
    def is_catPrime(p1, p2):
        return (
            primes_p[int(str(p1) + str(p2))]
            and primes_p[int(str(p2) + str(p1))]
        )

    def is_all_catPrime(p, primes):
        return (
            True if primes == [] else all(is_catPrime(p, p1) for p1 in primes)
        )

    # found はすでに prime pair set な素数のリスト
    def _find(found, cand_primes, cnt=5):
        if len(found) == cnt:
            ans.append(found)

        if len(cand_primes) == 0:
            return None

        for i, p in enumerate(cand_primes):
            if is_all_catPrime(p, found):
                new_found = _find(found + [p], cand_primes[i + 1 :], cnt)

                if new_found is not None:
                    return new_found
        return None

    primes = eratosthenes(lim, True)
    primes_p = eratosthenes(lim**2, False)

    # 明らかに p = 2, p = 5 は使わない
    del primes[0]
    del primes[1]

    ans = []

    for i in range(len(primes)):
        _find([primes[i]], primes[i + 1 :], cnt)
    return min(map(sum, ans))


def main():
    lim = 10**4
    N = 5
    return find(lim, N)


if __name__ == '__main__':
    print(main())
