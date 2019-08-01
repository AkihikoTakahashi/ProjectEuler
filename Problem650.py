# coding: utf-8

# B(n) = nC0 * nC1 * nC2 * ... * nCn
#      = n! / 0!(n-0)! * n! / 1!(n-1)! * n! / 2!(n-2)! * ... * n! / n!(n-n)!
#      = n!^(n+1) / (0!*1!*2!* ... * n!)^2
#      = {(n-1)!^n / (0!*1!*2!* ... * (n-1)!)^2} * (n-1)! * n^(n+1) / n!^2
#      = B(n-1) * n^n / n!
# B(n) は n 以下の素因数の積と商で書けるので, 最大の素数は n 以下である.
#
# 次に D(n) について考える.
# σ(n) = n の約数の和とする
# σ(p^e) = (p^(e+1) - 1) / (p - 1)
# 以上より,
# D(n) = σ(B(n)) = σ(B(n-1)) * σ(n^n / n!)
# と書ける.
#
# よって B(n) がどのように素因数分解されるかを調べればよい.
#
# n = Πp[i]^e[i] と書き, factor(n) := [e[0], e[1], ..., e[k]
# と定義し,
# factor(n) + factor(m) は辞書のキーの追加またはキーの和
# factor(n) - factor(m) は辞書のキーの差
# factor(n)^a = [p[0]:a*e[0], p[1]:a*e[1], ..., p[k]:a*e[k]] で定める.
#
# n * m = factor(n) + factor(m), n / m = facotr(n) - factor(m) である.
# factor(B(n)) = factor(B(n-1)) + factor(n)^n - factor(n!)

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

    return [i for i, p in enumerate(primes) if p]


@memo
def B(n):
    if n == 1:
        return {}
    else:
        nn = {p: n * e for p, e in val2dict(n).items()}
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
        for p, e in es.items():
            sum_d = sum_d * (pow(p, e + 1, m) - 1) * inverse(p - 1) % m
        return sum_d


@memo
def factorial(n):
    if n == 1 or n == 0:
        return {}
    else:
        return es_add(factorial(n - 1), val2dict(n))


def val2dict(n):
    es = dict()
    for p in primes:
        cnt_p = 0
        while n % p == 0:
            cnt_p += 1
            n //= p
        es[p] = cnt_p
        if n == 1:
            break
    return es


def es_add(e1, e2):
    es = e1.copy()
    for p, e in e2.items():
        if p in es:
            es[p] += e
        else:
            es[p] = e
    return es


def es_sub(e1, e2):
    es = e1.copy()
    for p, e in e2.items():
        es[p] -= e
    return es


N = 20000
m = 10**9 + 7
primes = eratosthenes(N)


def main():
    s = 0
    for i in range(1, N + 1):
        s = (s + D(i)) % m
    return s


if __name__ == "__main__":
    print(main())
