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
# ゆえに, 方程式の解が 1000 個以上 <==> n の約数が 1000 個以上 <==>
# n^2 の約数が 2000 個以上
# 平方数の約数の個数は奇数なので n^2 の約数が 2001 個以上となる
# 最小の n を見つければよい.
#
# n^2 の各素因数の指数は偶数なので, n^2 = Πa^(2e) となり, n^2 の約数の個数は
# Π(1+2e) である. よって, 1+2e >= 3 となり, 3^7 = 2187 > 2000 から必要な
# 素数は 7 個 (2, 3, 5, 7, 11, 13, 17) である.

from queue import PriorityQueue


def gen_prime():
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0:
            return False
        else:
            return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])

    i = 3
    yield 2

    while True:
        if is_prime(i):
            yield i
        i += 2


def main():
    pq = PriorityQueue()


if __name__ == "__main__":
    print(main())
