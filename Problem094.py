# coding: utf-8

# 辺の長さがそれぞれ (x, x, x+1) とするとヘロンの公式から
# S = (s(s - x)^2(s - x - 1))^(1/2), s = (3x - 1)/2
# となり, 整理すると
# S = (x + 1)/2 * ((3x +1)/2 * (x - 1)/2)^(1/2)
# よって x は奇数なので, x = 2n + 1 とすると,
# S = (n + 1) * (n(3n + 2))^(1/2) となる.  (n > 0)
#
# n(3n + 2) は平方数となるので, n(3n + 2) = y^2 とする.
#
# 3n^2 + 2n - y^2 = 0
# 9n^2 + 6n - 3y^2 = 0
# (3n + 1)^2 - 3y^2 = 1
#
# よって ペルの方程式 X^2 - 3Y^2 = 1 をの解(a, b) に対し,
# 3n + 1 = a ==> n = (a - 1)/3 ==> x = (2a + 1)/3 ==> 辺の合計 = 2a + 2
# また n > 0 から a >= 4 である.
#
#
# 辺の長さがそれぞれ (x, x, x-1) の場合も同様にして,
# S = n((3n + 1)(n + 1))^(1/2)  (x = 2n + 1, n > 0)
# (3n + 1)(n + 1) = y^2 として, ペルの方程式の形に変形すると,
#
# (3n + 2)^2 - 3y^2 = 1
#
# よって ペルの方程式 X^2 - 3Y^2 = 1 の解(a, b) に対し,
# 3n + 2 = a ==> n = (a - 2)/3 ==> x = (2a - 1)/3 ==> 辺の合計 = 2a - 2
# また n > 0 から a >= 5 である.
#
# まとめると,
# ペルの方程式 X^2 - 3Y^2 = 1 の解(a, b) に対し,
# a = 1 mod 3 なら 辺の合計 = 2a + 2
# a = 2 mod 3 なら 辺の合計 = 2a - 2
# ただし a >= 4


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
    lim = 1000000000
    s = 0
    for a, b in solve_pell_equation(3):
        if a < 4:
            continue

        if a % 3 == 1:
            if 2 * a + 2 > lim:
                break

            s += 2 * a + 2
        elif a % 3 == 2:
            if 2 * a - 2 > lim:
                break

            s += 2 * a - 2
    return s


if __name__ == '__main__':
    print(main())
