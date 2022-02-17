# coding: utf-8

from itertools import count, islice


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


def main():
    cnt = 10001
    return next(islice(gen_primes(), cnt - 1, None))


if __name__ == "__main__":
    print(main())
