# coding: utf-8

# (a + b)**2 < 10^N => a + b < 10^(N/2) => a < 10^(N/2), b < 10^(N/2)
# b を d 桁とすると, 数の結合 ab は 10^d * a + b と書ける.
# a についての方程式 10^d * a + b = (a + b)^2 を整理すると,
# a^2 + (2b - 10^d)a + b^2 - b = 0
# 判別式 D = 4b(1 - (10^d)) + 10^2d が平方数なら
# a = (10^d - 2b ± √D) / 2
# が解となる.
# また, D >= 0 より b は
# 4b(1 - (10^d)) + 10^2d >= 0
# を満す.
# これを整理すると b <= 10^2d / 4(10^d - 1) <= 10^2d / 4 * 10^d = 10^d / 4
# が言える.


def is_square(n):
    return int(n**0.5) ** 2 == n


def main():
    N = 16
    s = 0
    for b in range(1, pow(10, N // 2) // 4 + 1):
        d = len(str(b))
        det = 4 * b * (1 - pow(10, d)) + pow(10, 2 * d)
        if det < 0:
            continue
        if not is_square(det):
            continue
        a1 = int((pow(10, d) - 2 * b + det**0.5) // 2)
        a2 = int((pow(10, d) - 2 * b - det**0.5) // 2)
        if a1 > 0:
            s += a1 * pow(10, d) + b
        if a2 > 0:
            s += a2 * pow(10, d) + b
    return s


if __name__ == '__main__':
    print(main())
