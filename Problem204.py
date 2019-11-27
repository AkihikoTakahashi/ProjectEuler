# coding: utf-8


def eratosthenes(n):
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    return [i for i, p in enumerate(primes) if p]


def main():
    N = 10**9
    t = 100

    hammings = [True] * (N + 1)

    primes = eratosthenes(N)
    for p in primes:
        if p <= t:
            continue

        for i in range(p, N + 1, p):
            hammings[i] = False

    return sum(1 for i in hammings[1:] if i)


if __name__ == "__main__":
    print(main())
