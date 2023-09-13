# coding: utf-8

from itertools import product


def gen_ternary_as_dec():
    yield 1
    yield 2
    saved = [1, 2]

    while True:
        new_saved = []
        for n, i in product(saved, range(3)):
            yield 10 * n + i
            new_saved.append(10 * n + i)

        saved = new_saved


def f(n):
    if n % 10 == 0:
        return 10 * f(n//10)

    if n == 9999:
        return 11112222222222222222

    for t in gen_ternary_as_dec():
        if t % n == 0:
            return t


def main():
    n = 10000
    return sum(f(i) // i for i in range(1, n + 1))


if __name__ == '__main__':
    print(main())
