# coding: utf-8

from itertools import count, takewhile, islice


def ex_sieve(L=1000):
    a = [True] * L
    for p in (i for i in range(2, L) if a[i]):
        for k in range(2 * p, L, p):
            a[k] = False

    primes = [p for p in range(2, L) if a[p]]

    for p in primes:
        yield p

    for m in count(1):
        start = m * L
        end = start + L

        a = [True] * L
        for p in takewhile(lambda p: p * p < end, primes):
            k0 = (start + p - 1) // p * p - start
            for k in range(k0, L, p):
                a[k] = False

        for p in (start + k for k in range(L) if a[k]):
            primes.append(p)
            yield p


def main():
    cnt = 10001
    return next(islice(ex_sieve(), cnt - 1, None))


if __name__ == "__main__":
    print(main())
