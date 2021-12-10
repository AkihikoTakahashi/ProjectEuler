# coding: utf-8

# Problem137 と同様に判別式を求めると
# D = 5n^2 + 14n + 1
# D が平方数になればよいから,
# 5n^2 + 14n + 1 = m^2 を解く (n>0, n, m:整数)
#
# https://www.alpertron.com.ar/QUAD.HTM
# 上記サイトによると,
# 初期解は (n, m) = (2, -7), (0, -1), (0, 1), (-4, 5), (-3, 2), (-3, -2)
# n, m の漸化式は
# n_k+1 = -9 * n_k - 4 * m_k - 14,
# m_k+1 = -20 * n_k - 9 * m_k - 28
# または
# n_k+1 = -9 * n_k + 4 * m_k - 14,
# m_k+1 = 20 * n_k - 9 * m_k + 28
#
# よって, それぞれの初期解と漸化式にて 30 個ずつ解をリストに格納し,
# 先頭の 30 個の結合をとれば十分.


def main():
    cnt_max = 30
    starts = [(2, -7), (0, -1), (0, 1), (-4, 5), (-3, 2), (-3, -2)]
    nuggets = []

    for n, m in starts:
        for _ in range(cnt_max):
            n, m = -9 * n - 4 * m - 14, -20 * n - 9 * m - 28
            if n > 0 and n not in nuggets:
                nuggets.append(n)

    for n, m in starts:
        for _ in range(cnt_max):
            n, m = -9 * n + 4 * m - 14, 20 * n - 9 * m + 28
            if n > 0 and n not in nuggets:
                nuggets.append(n)

    nuggets.sort()
    return sum(nuggets[:cnt_max])


if __name__ == '__main__':
    print(main())
