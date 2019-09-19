# coding: utf-8


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
    N = 50000000
    squares = [
        i**2 for i in gen_eratosthenes(int(N**(1 / 2)))
        if i**2 + 2**3 + 2**4 < N
    ]
    triples = [
        i**3 for i in gen_eratosthenes(int(N**(1 / 3)))
        if i**3 + 2**2 + 2**4 < N
    ]
    fourth = [
        i**4 for i in gen_eratosthenes(int(N**(1 / 4)))
        if i**4 + 2**2 + 2**3 < N
    ]

    return len(
        set(s + t + f for s in squares for t in triples for f in fourth
            if s + t + f < N))


if __name__ == '__main__':
    print(main())
