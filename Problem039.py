# coding: utf-8

# 基本ピタゴラス数は
# gcd(m, n) = 1, m と n の偶奇がことなるとき,
# a = m**2 - n**2, b = 2 * m * n , c = m**2 + n**2
# で生成される.


# a**2 + b**2 = c**2, a + b + c <= x
# となる (a, b, c) を生成する.
def gen_pythagoras(x):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

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
    sum_a_b_c = 1000
    pythagoras = {i: 0 for i in range(sum_a_b_c + 1)}
    for a, b, c in gen_pythagoras(sum_a_b_c):
        pythagoras[a + b + c] += 1

    return max(pythagoras, key=pythagoras.get)


if __name__ == "__main__":
    print(main())
