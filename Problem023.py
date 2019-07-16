# coding: utf-8

# 2つの過剰数の和の合計を 1~28123 の和から引く.

from itertools import combinations_with_replacement


def factor_sum(n):
    from functools import reduce
    properDivisor = list(
        set(
            reduce(list.__add__, [[i, n // i]
                                  for i in range(1,
                                                 int(n**0.5) + 1)
                                  if n % i == 0])))
    del properDivisor[properDivisor.index(n)]

    return sum(properDivisor)


def is_abundant(n):
    return n < factor_sum(n)


def main():
    max_i = 28123

    abundants = [i for i in range(2, max_i + 1) if is_abundant(i)]
    sum_2_abundants = sum(
        set(i + j for i, j in combinations_with_replacement(abundants, 2)
            if i + j <= max_i))
    sum_all = (1 + max_i) * max_i // 2

    return sum_all - sum_2_abundants


if __name__ == "__main__":
    print(main())
