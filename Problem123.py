# coding: utf-8

# Problem120.pyと同様に
# (p[n] - 1)^n + (p[n] + 1)^n = 2 * p[n] * n mod p[n]^2 (n: 奇数)

from itertools import count


def gen_primes():
    yield 2
    primes = [2]

    for n in count(3, step=2):
        for p in primes:
            if n % p == 0:
                break
            if p * p > n:
                yield n
                primes.append(n)
                break


def calc(n, p):
    return 2 * p * n % p**2 if n % 2 == 1 else 2


def main():
    limit = 10**10

    return next(n for n, p in enumerate(gen_primes(), start=1)
                if calc(n, p) > limit)


if __name__ == "__main__":
    print(main())
