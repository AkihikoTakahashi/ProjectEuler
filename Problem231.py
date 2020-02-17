# coding: utf-8

# nCr = n!/r!(n-r)!
# a/bの素因数の和 = a の素因数の和 - b の素因数の和を用いる.


def get_minimum_factors(n):
    factors = [0] * (n + 1)
    lim = int(n**0.5) + 1

    for i in range(2, n + 1):
        if factors[i] != 0:
            continue

        factors[i] = i
        if i > lim:
            continue

        for j in range(i**2, n + 1, i):
            if factors[j] == 0:
                factors[j] = i
    return factors


def main():
    def factorial_factor_sum(n):
        s = 0
        for i in range(2, n + 1):
            while i > 1:
                j = minimum_factors[i]
                s += j
                i //= j
        return s

    N = 20000000
    R = 15000000
    minimum_factors = get_minimum_factors(N)

    return factorial_factor_sum(N) - factorial_factor_sum(
        R) - factorial_factor_sum(N - R)


if __name__ == '__main__':
    print(main())
