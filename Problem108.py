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
# ゆえに, 方程式の解が 1000 個以上 <==> n^2 の約数が 2000 個以上 が成り立つ.
# 平方数の約数の個数は奇数なので n^2 の約数が 2001 個以上となる
# 最小の n を見つければよい.
#
# n^2 の各素因数の指数は偶数なので, n^2 = Πa^(2e) となり, n^2 の約数の個数は
# Π(1+2e) である. よって, 1+2e >= 3 となり, 3^7 = 2187 > 2000 から必要な
# 素数は 7 個 (2, 3, 5, 7, 11, 13, 17) である.

from queue import PriorityQueue


# Π(e[i]+1) >= d となる e を返す
def next_e(e, cnt_d):
    e[0] //= 4
    e[1] += 2


def main():
    from functools import reduce

    def count_divisor(es):
        return reduce(lambda x, y: x * y, [x + 1 for x in es])

    def val(es, primes):
        return reduce(lambda x, y: x * y, [p**e for p, e in zip(primes, es)])

    e2 = [2, 2, 2, 2, 2, 2, 2]


if __name__ == "__main__":
    print(main())
