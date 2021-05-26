# coding: utf-8

# p(k) = p(k-1) + p(k-2) - p(k-5) - p(k-7) + p(k-12) + p(k-15) ...
# 1, 2, 5, 7, ... は拡張五角数
#
# https://ja.wikipedia.org/wiki/%E5%88%86%E5%89%B2%E6%95%B0

from itertools import count, takewhile, cycle


def gen_ex_pentagonal():
    '''拡張五角数を生成する.'''
    for k in count(1):
        n = (3 * k - 1) * k // 2
        yield n

        # f(k) = (3k^2 - k) / 2 ==>
        # f(-k) = (3k^2 + k) / 2 ==>
        #       = f(k) + k
        n += k
        yield n


def main():
    N = 10**6
    partitions = [1]
    signs = (1, 1, -1, -1)
    for n in count(1):
        p_n = 0
        for sign, k in zip(cycle(signs),
                           takewhile(lambda k: k <= n, gen_ex_pentagonal())):
            p_n = (p_n + sign * partitions[n - k]) % N
        if p_n == 0:
            return n
        partitions.append(p_n)


if __name__ == '__main__':
    print(main())
