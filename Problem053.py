# coding: utf-8

from math import factorial


def main():
    def comb(n, r):
        return facts[n] // (facts[r] * facts[n - r])

    L = 1000000
    n_lim = 100
    facts = [factorial(i) for i in range(n_lim + 1)]

    return sum(
        comb(n, r) > L for n in range(1, n_lim + 1) for r in range(n + 1))


if __name__ == '__main__':
    print(main())
