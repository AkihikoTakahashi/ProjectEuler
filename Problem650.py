# coding: utf-8

# B(n) = nC0 * nC1 * nC2 * ... * nCn
#      = n! / 0!(n-0)! * n! / 1!(n-1)! * n! / 2!(n-2)! * ... * n! / n!(n-n)!
#      = n!^(n+1) / (0!*1!*2!* ... * n!)^2
#      = {(n-1)!^n / (0!*1!*2!* ... * (n-1)!)^2} * (n-1)! * n^(n+1) / n!^2
#      = B(n-1) * n^n / n!
#
# σ(n) = n の約数の和とする
# σ(p^e) = (p^(e+1) - 1) / (p - 1)
# D(n) = σ(B(n)) = σ(B(n-1)) * σ(n^n / n!)
#
# n = Πp[i]^e[i] と書き, factor(n) := [e[0], e[1], ..., e[k]
# と定義し,
# factor(n) + factor(m) はリストのそれぞれの要素の和
# factor(n) - factor(m) はリストのそれぞれの要素の差
# factor(n)^a = [a*e[0], a*e[1], ..., a*e[k]] で定める.
#
# n * m = factor(n) + factor(m), n / m = facotr(n) - factor(m) である.
# factor(B(n)) = factor(B(n-1)) + factor(n)^n - factor(n!)
# n! の p の指数は n//p + n//p^2 + n//p^3 + n//p^4 + ... である.

from functools import reduce


def memo(f):
    check = {}

    def func(*args):
        if args not in check:
            check[args] = f(*args)
        return check[args]

    return func


def eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return primes


@memo
def B(n):

    if n == 1:
        return [0] * len(primes)
    else:
        nn = [n * i for i in val2list(n)]
        fact_n = factorial(n)
        return es_sub(es_add(B(n - 1), nn), fact_n)


@memo
def inverse(n, m=10**9 + 7):
    return pow(n, m - 2, m)


def D(n):
    if n == 1:
        return 1
    else:
        es = B(n)
        sum_d = 1
        for p, e in zip(primes, es):
            sum_d = sum_d * (pow(p, e + 1) - 1) // (p - 1) % m
        return sum_d


@memo
def factorial(n):
    if n == 1 or n == 0:
        return [0] * len(primes)
    else:
        return es_add(factorial(n - 1), val2list(n))

    # es = [0] * len(primes)
    # for i, p in enumerate(primes):
    #     e = 0
    #     tmp_p = p
    #     if n < p:
    #         break
    #     while n >= p:
    #         e += n // p
    #         p *= tmp_p
    #     es[i] = e
    # return es


def val2list(n):
    es = [0] * len(primes)
    for i, p in enumerate(primes):
        cnt_p = 0
        while n % p == 0:
            cnt_p += 1
            n //= p
        es[i] = cnt_p
        if n == 1:
            break
    return es


def list2val(es, m=1000000007):
    return reduce(lambda x, y: x * y % m,
                  [pow(p, e, m) for p, e in zip(primes, es)])


def es_add(e1, e2):
    return [a + b for a, b in zip(e1, e2)]


def es_sub(e1, e2):
    return [a - b for a, b in zip(e1, e2)]


N = 20000
m = 10**9 + 7
primes_bool = eratosthenes(N)
primes = [i for i, p in enumerate(primes_bool) if p]


def main():
    return sum(D(i) for i in range(1, N + 1)) % m


if __name__ == "__main__":
    print(main())
