# coding: utf-8

from itertools import permutations


def main():
    perm = permutations(range(0, 10), 10)

    for i in range(1000000):
        list_n = next(perm)

    n = 0
    for i in list_n:
        n = n * 10 + i
    return n


if __name__ == "__main__":
    print(main())
