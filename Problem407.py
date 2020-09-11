# coding: utf-8

# a^2 = a mod p となる最大の a を求める.
#
# p = n^e のとき
# a(a - 1) = 0 mod p であり, a, a-1 は互いに素なので,
# a = 0 または a = 1
#
# p = n^e * m^f のとき
# F: Z/pZ ---> Z/n^eZ * Z/m^fZ
# F(x mod p) = (x mod n^e, x mod m^f)
# と F を定義すると
# a = max(F^-1(i, j) i,j=0,1 である.
#
# また a^2 = a mod p なら b = -a + 1 も b^2 = b mod p
# を満す.

from itertools import product, islice

log = {}


def exgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    q, r = a // b, a % b
    (g, u1, v1) = exgcd(b, r)
    u0 = v1
    v0 = u1 - q * v1

    return (g, u0, v0)


def crt(*eqs):
    from functools import reduce
    return reduce(_crt, eqs, (0, 1))[0]  # mod n は不要


def _crt(eq0, eq1):
    a0, m0 = eq0
    a1, m1 = eq1

    if (m0, m1) not in log:
        log[(m0, m1)] = exgcd(m0, m1)

    d, u, v = log[(m0, m1)]
    if (a0 - a1) % d != 0:
        raise Exception("x doesn't exists")

    s = (a1 - a0) // d
    m = m0 * m1 // d
    x = (a0 + m0 * s * u) % m

    return (x, m)


# n 以下の数の最小の素因数を取得
def osa_k(n):
    min_factors = [-1, -1] + [i for i in range(2, n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if min_factors[i] == i:
            for j in range(i**2, n + 1, i):
                if min_factors[j] == j:
                    min_factors[j] = i

    return min_factors


def factorization(n):
    min_factors = osa_k(n)
    factors = [None, None]  # 0, 1 は素因数分解できない
    for i in range(2, n + 1):
        f_i = []
        while i > 1:
            f = 1
            while True:
                tmp = min_factors[i]
                f *= tmp
                i //= tmp
                if min_factors[i] != tmp:
                    break
            f_i.append(f)
        factors.append(f_i)
    return factors


def main():
    LIM = 10**7
    factors = factorization(LIM)
    s = 0
    for fs in factors[2:]:  # mod 1 のとき a = 0
        idempotents_i = []
        if len(fs) == 1:
            s += 1
            continue

        # fs = [2, 3, 5]
        # max(crt((0,2),(0,3),(1,5)), crt((0,2),(1,3),(0,5)),
        #     crt((1,2),(0,3),(0,5)), crt((0,2),(1,3),(1,5)),
        #     crt((1,2),(0,3),(1,5)), crt((1,2),(1,3),(0,5)))
        for i in product((0, 1), repeat=len(fs)):
            if all(x == 0 for x in i) or all(x == 1 for x in i):
                continue
            c = [n for n in islice(zip(i, fs), len(fs))]
            idempotents_i.append(crt(*c))
        s += max(idempotents_i)
    return s


if __name__ == '__main__':
    print(main())
