# coding: utf-8

# 1/x + 1/y = 1/n
#
# n = 4 なら
# 1/5 + 1/20 = 1/4
# 1/6 + 1/12 = 1/4
# 1/8 + 1/8 = 1/4
# の3つ
#
# x, y の対称性より x <= y として問題ない.
#
# 1/x + 1/y = 1/n <=> yn + xn = xy
# xy - xn - yn + n^2 = n^2
# (x - n)(y - n) = n^2
# よって x - n, y - n は n^2 の約数.
# ゆえに, 方程式の解が 4 * 10^6 個以上 <==> n^2 の約数が 8 * 10^6 個以上 が成り立つ.
# 平方数の約数の個数は奇数なので n^2 の約数が 8 * 10^6 + 1 個以上となる
# 最小の n を見つければよい.
#
# n^2 の各素因数の指数は偶数なので, n^2 = Πa^(2e) となり, n^2 の約数の個数は
# Π(1+2e) である. よって, 1+2e >= 3 となり, 必要な素数は
# int(log_3(8 * 10^6)) + 1 = 15 個
# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
# である.
#
# k 種類の素数の次数が 2 個持つ場合, 約数の個数は
# 5^k であり 8 * 10^6 を超える最小の k は 10 となる.
# よって, 素数は少なくとも 10 個以上必要であり,
# n は少なくとも, 小さい素数から順に 10 個掛けた値の倍数である.
#
from math import log


def get_primes(n):
    '''素数を n 個返す'''
    from itertools import takewhile

    primes = [2]
    i = 3
    while len(primes) < n:
        for p in takewhile(lambda p: p * p <= i, primes):
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 2
    return primes


def count_divisor(n, primes):
    from functools import reduce

    es = [0] * len(primes)

    # n をすべての素数で割り尽くし, 残りが 1 でなければそれ以外の素数を含む.
    for i in range(len(primes)):
        p = primes[i]
        while n % p == 0:
            n //= p
            es[i] += 1

    if n == 1:
        return reduce(lambda x, y: x * y, [e + 1 for e in es])
    else:
        return 0


def main():
    N = 4 * 10**6
    primes = get_primes(int(log(2 * N, 3)) + 1)
    k = int(log(2 * N, 5)) + 1
    add = 1
    for i in primes[:(k + 1)]:
        add *= i
    n = add
    while count_divisor(n**2, primes) < 8 * 10**6:
        n += add
    return n


if __name__ == "__main__":
    print(main())
