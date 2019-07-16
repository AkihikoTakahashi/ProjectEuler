# coding: utf-8


def Eratosthenes(n):
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(int(n**0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


def main():
    lim_sum = 1000000
    primes = Eratosthenes(lim_sum)
    len_primes = len(primes)
    max_len = 1
    max_s = 0

    for i in range(len_primes):
        j = max_len
        s = sum(primes[i:i + j])

        # primes[i] を max_len 個掛けて lim_sum を超たら, 以降に解の候補なし
        if primes[i] * max_len > lim_sum:
            break

        while i + j < len_primes:
            s += primes[i + j]
            if s > lim_sum:
                break

            if s in primes and max_len < j + 1:
                max_len = j + 1
                max_s = s

            j += 1
    return max_s


if __name__ == "__main__":
    print(main())
