# coding: utf-8


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2

    if n != 1:
        factors.append(n)
    return factors


def main():
    n = 600851475143
    return prime_factors(n)[-1]


if __name__ == "__main__":
    print(main())
