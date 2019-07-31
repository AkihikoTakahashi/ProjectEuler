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
# n = Πp[i]^e[i] と書き, factor(n) := {p[0]:e[0], p[1]:e[1], ..., p[k]:e[k]}
# と定義し,
# factor(n) + factor(m) は辞書のキーの和またはキーの追加,
# factor(n) - factor(m) は辞書のキーの差またはキーの削除,
# factor(n)^a = {p[0]:a*e[0], p[1]:a*e[1], ..., p[k]:a*e[k]} で定める.
#
# n * m = factor(n) + factor(m), n / m = facotr(n) - factor(m) である.
# factor(n!) = factor((n-1)!) + factor(n)
# factor(B(n)) = factor(B(n-1)) + factor(n)^n - factor(n!)

from functools import lru_cache, reduce


@lru_cache(maxsize=256)
def B(n):
    if n == 1:
        return 1
    else:
        return B(n - 1) * n**n // reduce(lambda x, y: x * y, range(1, n + 1))


def D(n):
    pass


# n! を素因数分解した形で返す
@lru_cache(maxsize=256)
def factorial(n, e_dict={}):
    if n == 1:
        return e_dict
    else:
        return factorial(n - 1, dict_add(e_dict, val2dict(n)))


def val2dict(n):
    pass


def dict2val(es, m=1000000007):
    return reduce(lambda x, y: x * y % m,
                  [pow(p, e, m) for p, e in es.items()])


def dict_add(d1, d2):
    d = d1.copy()
    for k, v in d2.items():
        if k in d:
            d[k] += v
        else:
            d[k] = v
    return d


def dict_sub(d1, d2):
    d = d1.copy()
    for k, v in d2.items():
        if k in d:
            d[k] -= v
            if d[k] == 0:
                del d[k]
        else:
            d[k] = -v
    return d


def main():
    pass


if __name__ == "__main__":
    print(main())
