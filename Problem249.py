# coding: utf-8


def eratosthenes(n):
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    return primes


def main():
    N = 5000
    MOD = 10**16
    primes = [i for i, p in enumerate(eratosthenes(N)) if p]

    # dp[i] には素数を足して i になる部分集合の個数をいれる
    dp = [0] * (sum(primes) + 1)
    dp[0] = 1
    s = 0  # s は素数の和が入る

    for p in primes:
        for i in range(s, -1, -1):
            dp[p + i] = (dp[p + i] + dp[i]) % MOD
        s += p

    is_primes = eratosthenes(s)
    cnt = sum(dp[i] for i in range(s + 1) if is_primes[i]) % MOD
    return cnt


if __name__ == '__main__':
    print(main())
