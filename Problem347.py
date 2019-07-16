# coding: utf-8

# M(p, q, N) を求める. p, q は p<q となる素数としても一般性を失わない.
# N は p, q で割り切れるため, n = p * q とする.
# n に n * p^i <= N < n * p^(i+1) となるように p^i を掛ける. (最大値候補)
# n を p で割り, N を越えないように q^j を掛ける. (★) (最大値候補)
# (★) の手順を n/p が p で割り切れなくなるまで繰り返す.
# 最大値候補のなかで最大値が M(p, q, N) の解となる.


def eratosthenes(n):

    is_prime = [False if i % 2 == 0 else True for i in range(n + 1)]
    is_prime[0], is_prime[1], is_prime[2] = False, False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime[i]:
            for i in range(2 * i, n + 1, i):
                is_prime[i] = False

    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


def M(p, q, N):
    n = p * q

    while n * p <= N:
        n *= p

    max_n = n
    while (n // p) % p == 0:
        n //= p
        while n * q <= N:
            n *= q
        max_n = max(n, max_n)

    return max_n


def main():
    N = 10000000
    lim = int(N**0.5) + 1
    s = 0
    primes = eratosthenes(N // 2)

    for i in range(len(primes)):
        p = primes[i]

        # p > lim なら p * q > N なので解なし.
        if p > lim:
            break

        for j in range(i + 1, len(primes)):
            q = primes[j]

            # p * q > N なら次の素数 p の検索を開始する.
            if p * q > N:
                break

            s += M(p, q, N)

    return s


if __name__ == "__main__":
    print(main())
