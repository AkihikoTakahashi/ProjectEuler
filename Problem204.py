# coding: utf-8

# ハミング数の集合を H, type=100 とし, type 以下の素数を p_1, p_2, ...,  とする.
# ハミング数の初期値を H = {1} であり, p_1 ^ n <= N を H に追加する.
# h を H の要素とし, h * p_2 ^ n <= N となる h * p_2 ^ n を H に追加する.
# これをすべての p_i で繰り返すと, すべての
# p_1 ^ e_1 * p_2 ^ e_2 * ... * p_k ^ e_k <= N が得られる.


def eratosthenes(n):
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    return [i for i, p in enumerate(primes) if p]


def main():
    h_type = 100
    primes = eratosthenes(h_type)
    N = 10**9

    hammings = [1]

    for p in primes:
        factors = []
        for h in hammings:
            x = p * h
            while x <= N:
                factors.append(x)
                x *= p
        hammings += factors
    return len(hammings)


if __name__ == "__main__":
    print(main())
