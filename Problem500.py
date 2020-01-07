# coding: utf-8

# 2^4個の約数を持つには
#
# p[1]^15 --> 1+15
# p[1]^7 * p[2] --> (1+7) * (1+1)
# p[1]^3 * p[2]^3 --> (1+3) * (1+3)
# p[1]^3 * p[2] * p[3] --> (1+3) * (1+1) * (1+1)
# p[1] * p[2] * p[3] * p[4] --> (1+1) * (1+1) * (1+1) * (1+1)
#
# の5通りある. 最小を求めるので, p1=2, p2=3, p3=5, ... と小さい素数から割り当てる.
#
#
# n が 2^500500 個の約数を持つには,
# n = Πp[i]^e[i] (p[i]は素数)
# Π(e[i]+1) = 2^500500
# と書ける. また, e[i]+1 は 2^k という形で書ける.
#
# よって, 2^500500 個の約数を持つには
# n = Πp[i]^(k[i])
# ただし
# k[i] は 2ベキ-1 かつ, Σk[i] = 500500
#
# 必要となる素数は
# n = p[1] * p[2] * p[3] * ... * p[500500]
# のときで, 500500 番目の素数までで十分である.
# 500500 番目の素数は 7676507 である.
#
# 2^1個の約数を持つ数は 2^1
# 2^2     〃            2^1 * 3^1
# 2^3     〃            2^3 * 3^1
# 2^4     〃            2^3 * 3^1 * 5^1
# 2^5     〃            2^3 * 3^1 * 5^1 * 7^1
# 2^6     〃            2^3 * 3^3 * 5^1 * 7^1
# 2^7     〃            2^3 * 3^3 * 5^1 * 7^1 * 11^1
# 2^8     〃            2^3 * 3^3 * 5^1 * 7^1 * 11^1 * 13^1
# 2^9     〃            2^7 * 3^3 * 5^1 * 7^1 * 11^1 * 13^1
#
# 2^(a-1)個の約数を持つ数を 2^e[1] * 3^e[2] * 5^e[3] * ... p[i]^e[i] とすると,
# 2^a 個の約数を持つ数は使っていない最小の素数を掛ける, または最小の
# (p[i]^e[i])^2 を掛ける.
#
# 処理の流れは以下のようになる.
# 1. 500500 番目までの素数リストを作る. 今回はメモリ節約のため
#    ジェネレータを利用.
# 2. ループ処理
# 2-1. 素因数リストから最小の要素を取り出し, 掛ける.
# 2-2. 取り出した要素の2乗を素因数リストに追加する.
# 2-3. 取り出した要素が素数の場合は, 次の素数を素因数リストに追加する.
#

import heapq


def gen_eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    for i in range(n + 1):
        if primes[i]:
            yield i


def main():
    max_e = 500500
    modulo = 500500507
    gen_primes = gen_eratosthenes(7376507)

    prod = 1
    next_prime = next(gen_primes)
    factors = [next_prime]

    for _ in range(max_e):

        n = heapq.heappop(factors)
        prod = (prod * n) % modulo
        heapq.heappush(factors, n**2)

        if n == next_prime:
            next_prime = next(gen_primes)
            heapq.heappush(factors, next_prime)

    return prod


if __name__ == "__main__":
    print(main())
