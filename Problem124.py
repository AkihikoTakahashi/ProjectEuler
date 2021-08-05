# coding: utf-8

# エラトステネスの篩の要領で rad(n) を計算する.
#
# 変数 rads を [None, 1, 1, 1, ...] で初期化し
# 2 の倍数番目の値に 2 を掛ける.
# rads = [None, 1, 2, 1, 2, 1, 2, ...]
#
# 3 の倍数番目の値に 3 を掛ける.
# rads = [None, 1, 2, 3, 2, 1, 6, ...]
#
# 4 番目は 1 ではないのでスキップ.
# 5 の倍数番目の値に 5 を掛ける.
# rads = [None, 1, 2, 3, 2, 5, 6, ...]
#
# 以降, i 番目が 1 であれば i の倍数番目の値に i を掛けることで,
# rads が計算できる.
#
# rads のソートは rads の値と要素番号でソートする.


def rad(n):
    rads = [None] + [1] * n
    for i in range(2, n + 1):
        if rads[i] == 1:  # i は素数
            for j in range(i, n + 1, i):
                rads[j] *= i
    return rads[1:]


def main():
    lim_n = 100000
    r = 10000
    rads = rad(lim_n)
    rads = [(r, i) for i, r in enumerate(rads, start=1)]

    sorted_rads = sorted(rads, key=lambda x: (x[0], x[1]))

    return sorted_rads[r - 1][1]


if __name__ == '__main__':
    print(main())
