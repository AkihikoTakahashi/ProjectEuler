# coding: utf-8

from math import gcd


def gen_pythagoras(x):

    for m in range(1, int((x // 2)**0.5) + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or m % 2 == n % 2:
                continue

            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            if a > b:
                a, b = b, a

            s = a + b + c
            for i in range(1, x // s + 1):
                yield a * i, b * i, c * i


def main():
    L = 1500000

    wire_len = [0] * (L + 1)

    pythagoras = gen_pythagoras(L)
    for a, b, c in pythagoras:
        wire_len[a + b + c] += 1

    return sum(map(lambda x: x == 1, wire_len))


if __name__ == '__main__':
    print(main())
