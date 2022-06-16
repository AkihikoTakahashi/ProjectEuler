# coding: utf-8

# u(k) = (900 - 3k)r^{k-1} の和 s(n) = u(1) + u(2) + ... + u(n) の一般項は
# s(n) = (900 - 3(1 - r^n) / (1 - r) - (a - nb)r^n) / (1 - r)
# である.
# r^5000 を概算する.
# r^5000 = y とすると, 5000*log10(r) = log10(y)
# r = 1.1 とすると log10(1.1) = 0.041 より 5000 * log10(1.1) > 206.9 なので
# r = 1.1 のとき r^5000 は 207 桁
# 同様に
# r = 1.01 のとき r^5000 は 22 桁
# r = 1.001 のとき r^5000 は 3 桁
# よって 1.001 < r < 1.009 である.


def s(r, n):
    a = 900
    b = 3

    if r != 1:
        return (a - b * (1 - r**n) / (1 - r) - (a - n * b) * r**n) / (
            1 - r
        )

    else:
        return 900 * n - 3 * n * (n + 1) / 2


def main():

    F = 12
    n = 5000
    N = -6e11
    r = 1.0
    for i in range(2, F + 1):  # 小数第1位, 2位は 0 確定
        for r_next in [r + d * pow(10, -i - 1) for d in range(1, 11)]:
            if s(r_next, n) < N:
                r = r_next - pow(10, -i - 1)
                break
    return round(r, F)


if __name__ == '__main__':
    print(main())
