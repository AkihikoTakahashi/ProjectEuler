# coding: utf-8

from functools import reduce


def sum_digit(n, s=0):
    if n == 0:
        return s
    else:
        return sum_digit(n // 10, s + n % 10)


def main():
    lim = 100
    fact = reduce(lambda x, y: x * y, range(1, lim + 1))
    return sum_digit(fact)


if __name__ == "__main__":
    print(main())
