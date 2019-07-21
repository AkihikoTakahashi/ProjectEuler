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
# よって x - n, y - n は n^2 の約数で, x - n <= y - n より, (x - n) < √(n^2) = n
# n < x <= 2n
#
# n = 4 のとき
# (x - 4)(y - 4) = 1*16, 2*8, 4*4
# (x, y) = (5, 20), (6, 12), (8, 8)
#
# よって, 解の個数は n の約数の個数と一致する.
# 1000個以上の解を持つ最小の n は約数の個数が 1000 を超える最小の n である.

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
