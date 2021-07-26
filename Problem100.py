# coding: utf-8

# 青を m, 全体を n とすると
# (m / n) * ((m-1) / (n-1)) = 1/2
# 整理すると
# n(n-1) = 2m(m-1)
# 4n(n-1) = 8m(m-1)
# (2n-1)^2 - 1 = 2(2m-1)^2 - 2
# (2n-1)^2 - 2(2m-1)^2 = -1
# よってペルの方程式 x^2 - 2y^2 = -1 ただしx, y は奇数
# を解き, 2m - 1 = y から m = (y + 1)/2 を得る.

from itertools import dropwhile


def check_pell(D, k=1):
    def f(x, y):
        return x * x - D * y * y == k

    return f


def cfrac(d):
    p, q = 0, 1
    x = int(d**0.5)

    while True:
        a = (x + p) // q
        yield a
        p = a * q - p
        q = (d - p * p) // q


def solve_pell_equation(D, k=1):
    pell_eq = check_pell(D, k)
    cf = cfrac(D)

    p0, q0 = 0, 1
    p1, q1 = 1, 0

    while True:
        if pell_eq(p1, q1):
            yield p1, q1
        a = next(cf)
        p1, p0 = a * p1 + p0, p1
        q1, q0 = a * q1 + q0, q1


def main():
    lim = 10**12
    _, y = next(dropwhile(lambda x: x[1] < lim, solve_pell_equation(2, -1)))
    m = (y + 1) // 2
    return m


if __name__ == '__main__':
    print(main())
