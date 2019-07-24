# coding: utf-8


# a**2 + b**2 = c**2, a + b + c <= x
# となる (a, b, c) を生成する.
def gen_pythagoras(x):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return b

    for m in range(1, int((x // 2)**0.5) + 1):
        for n in range(1, m):
            if gcd(m, n) != 0:
                continue

            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            if a > b:
                a, b = b, a

            s = a + b + c
            for i in range(1, x // s + 1):
                yield a * i, b * i, c * i
