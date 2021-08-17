# coding: utf-8

# Problem135と同様に解けるが 2min 近くかかる.
#
# Problem135と同様に uv = n, u + v = 0 mod 4, u <= 3v
# について, どのような n なら条件を満すか考える.
#
# 1. n が素数のとき,
# 1.1. n が n = 1 mod 4 のとき,
# (u, v) = (1, n) or (n, 1) だが, いずれも u + v != 0 mod 4
# より解なし.
#
# 1.2. n が n = 3 mod 4 のとき,
# (u, v) = (1, n) or (n, 1), u + v = 0 mod 4 を満し,
# u <= 3v から (u, v) = (1, n) だけが解となる.
# よって n が素数のとき n = 3 mod 4 のとき, 解は 1 つだけである.
#
# 2. n = 2^a * m (a と m は互いに素, a >= 1)
# 2.1. m が 1 または素数のとき
# (u, v) = (2^i, 2^(a-i) * m) (i = 1, 2, ..., a)
# u + v = 0 mod 4 となるには (2, 2m), または (4, 4m) のとき
# つまり, a = 2, 4 のとき, 解は 1 つだけである.
# 逆に a >= 5 のとき (u, v) = (4*2^i, 4 * 2^(a-2-i) * m) は
# u + v = 0 mod 4 を満し, 複数の解をもつ.
#
# 2.2. m が合成数 pq とき
# (u, v) = (2p, 2^(a-1) * q), (2, 2^(a-1) * pq) が
# u + v = 0 mod 4 を満し, 複数の解をもつ
#
# 3. n = p^a * q^b (p, q, は素数, a >= 0, b >= 0, p >= q) のとき
# 3.1. p = 1 mod 4, q = 1 mod 4 のとき
# u + v = 0 を満さないので, 解なし
#
# 3.2. p = 1 mod 4, q = 3 mod 4 のとき
# (u, v) = (1, pq), (p, q) が u + v = 0 mod 4 を満すので,
# 複数の解をもつ
#
# 3.3. p = 3 mod 4, q = 3 mod 4 のとき
# u + v = 0 を満さないので, 解なし
#
# すべてをまとめると, n = 4, 16, n = 3 mod 4 となる素数,
# 4p (p は 2 以外の素数), 16p (p は素数) のとき
# 等差数列 x^2 - y-2 - z^2 = n は唯一解をもつ,


def eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    p = [i for i in range(n + 1) if primes[i]]

    return p


def main():
    N = 50000000
    cnt = 2  # n = 4, 16 は条件を満す

    primes = eratosthenes(N)
    primes = primes[1:]  # 素数 2 を除く
    for p in primes:
        if p % 4 == 3:
            cnt += 1

        if p * 4 < N:
            cnt += 1
        if p * 16 < N:
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
