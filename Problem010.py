# coding: utf-8


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
    n = 2000000
    return sum(eratosthenes(n))


if __name__ == "__main__":
    print(main())
