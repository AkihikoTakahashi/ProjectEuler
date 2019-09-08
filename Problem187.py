# coding: utf-8


def eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]


def main():
    limit = 10**8
    primes = eratosthenes(limit // 2)
    n = len(primes)

    cnt = 0
    for n1 in range(n):
        for n2 in range(n1, n):
            if primes[n1] * primes[n2] > limit:
                break
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(main())
