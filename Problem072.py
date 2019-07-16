# coding: utf-8

# 分母が d 以下の既約真分数の個数は 2 <= i <= d なる i と互いに素となる数
# の個数の合計で求まる.
# 問題にあるように 1/8 の右隣は何かを気にする必要はない.
# i と互いに素となる数の個数はオイラーのφ関数を使って計算する.
#
# φ関数は以下の特徴を持つ.
#
#    φ(p^e) = p^e - p^(e-1)  (p は素数)
#    φ(p^e * a) = φ(p^e) * φ(a)  (p と a は互いに素)
#

from functools import lru_cache


def eratosthenes(N):

    is_prime = [False if i % 2 == 0 else True for i in range(N + 1)]
    is_prime[0], is_prime[1], is_prime[2] = False, False, True

    for i in range(3, int(N**0.5) + 1, 2):
        if is_prime[i]:
            for i in range(2 * i, N + 1, i):
                is_prime[i] = False

    return is_prime


@lru_cache(maxsize=None)
def phi(n):

    if n == 1:
        return 1

    if is_primes[n]:
        return n - 1

    else:
        i = 2
        tmp_n = n
        for i in range(2, n):
            if is_primes[i] and n % i == 0:
                e = 1
                while tmp_n % i == 0:
                    tmp_n //= i
                    e += 1
                e -= 1

                if tmp_n == 1:
                    return i**e - i**(e - 1)
                else:
                    return phi(i**e) * phi(n // (i**e))


def main():

    s = 0
    for i in range(2, d + 1):
        s += phi(i)
    return s


d = 1000000
is_primes = eratosthenes(d)

if __name__ == "__main__":
    print(main())
