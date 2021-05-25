# coding: utf-8

from functools import lru_cache
from itertools import count


def p(n):
    @lru_cache(maxsize=1024)
    def _p(k, n):
        if k > n:
            return 0
        if k == n:
            return 1
        else:
            return _p(k + 1, n) + _p(k, n - k)

    return _p(1, n)


def main():
    N = 10**6
    for i in count(1):
        if p(i) % N == 0:
            return i


if __name__ == '__main__':
    print(main())
