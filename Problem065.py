# coding: utf-8


def gen_cfrac_e():
    n = 1
    yield 2
    while True:
        yield 1
        yield 2 * n
        n += 1
        yield 1


def gen_frac():
    p1, p0 = 1, 0
    q0, q1 = 0, 1
    cf = gen_cfrac_e()
    while True:
        a = next(cf)
        p1, p0 = a * p1 + p0, p1
        q1, q0 = a * q1 + q0, q1
        yield (p1, q1)


def main():
    c = gen_frac()
    sum_numerator = 0
    for i in range(100):
        numerator = next(c)[0]

    while numerator > 0:
        sum_numerator += numerator % 10
        numerator //= 10
    return sum_numerator
