# coding: utf-8

# 21, 22, 23, 24, 25
# 20,  7,  8,  9, 10
# 19,  6,  1,  2, 11
# 18,  5,  4,  3, 12
# 17, 16, 15, 14, 13
#
# 辺の数の個数が n = 2m+1 のとき,
# 右上の頂点は n^2 であり, 左上, 左下, 右下の順に
# n-1 ずつ減る.
# サイズが 1001*1001 の対角線上の合計はサイズ 1, 2, 3, ... , 1001 の
# 各頂点の和を合計すればよい.


def sum_diagonals(size):
    rightup = size**2
    leftup = rightup - size + 1
    leftdown = leftup - size + 1
    rightdown = leftdown - size + 1

    return rightup + rightdown + leftup + leftdown


def main():
    size = 1001
    sum_diag = 1
    sum_diag += sum(sum_diagonals(i) for i in range(3, size + 1, 2))
    return sum_diag


if __name__ == "__main__":
    print(main())
