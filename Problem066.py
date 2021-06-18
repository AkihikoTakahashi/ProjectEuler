# coding: utf-8


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
    limit = 1000
    max_x = 1
    ans_d = 1

    for d in range(2, limit + 1):
        if int(d**0.5)**2 == d:
            continue
        pell = solve_pell_equation(d)
        x = next(pell)  # 自明解を除く
        x = next(pell)[0]
        if max_x < x:
            max_x = x
            ans_d = d
    return ans_d


if __name__ == '__main__':
    print(main())
