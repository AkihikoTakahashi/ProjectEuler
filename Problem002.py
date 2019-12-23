# coding: utf-8

from itertools import takewhile


def gen_fibo():
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


def main():
    lim = 4000000

    return sum(
        filter(lambda x: x % 2 == 0, takewhile(lambda x: x < lim, gen_fibo())))


if __name__ == "__main__":
    print(main())
