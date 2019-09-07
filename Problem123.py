# coding: utf-8

# Problem120.pyと同様に
# (p[n] - 1)^n + (p[n] + 1)^n = 2 * p[n] * n mod p[n]^2 (n: 奇数)


def gen_prime():
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0:
            return False
        else:
            return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])

    i = 3
    yield 2

    while True:
        if is_prime(i):
            yield i
        i += 2


def calc(n, p):
    return 2 * p * n % p**2 if n % 2 == 1 else 2


def main():
    primes = gen_prime()
    limit = 10**10

    return next(n for n, p in enumerate(primes, start=1) if calc(n, p) > limit)


if __name__ == "__main__":
    print(main())
