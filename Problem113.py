# coding: utf-8

# 5 桁以下の増加数を次のように考える.
#
# + | + + | + | + + | | + + +
#
# 0 で始まり + で 1 増加, | でそのときの値を桁の数とする.
# すると上の例は 13466 となる.
# このように作られた数はすべて増加数となる.
# 5 桁の増加数を作る方法は 9 個の + と 5 個の | の組み合わせなので,
# C(14, 5)と書ける. (14 個の枠から 5 箇所 | を置く場所を選ぶことと同義)
# ここから 0 (| | | | | + + + + + + + + +) を除き
# C(14, 5) - 1 が 5 桁以下の増加数の個数となる.
# n 桁以下の場合だと C(n + 9, n) - 1 = C(n + 9, 9) - 1 である.
#
# 同様に 5 桁の減少数を考える.
#
# - | - | | - - - - | - - | - -
#
# 10 で始まり - で 1 減少, | でそのときの値を桁の数とする.
# さらに 10 を 0 と置き換えることで 5 桁以下の減少数を作成できる.
# 上の例だと 98842 であり,
#
# | - | - | - | | - - - - - - -
#
# は 9877 である.
#
# - - - - - - - - - - | | | | |
# | - - - - - - - - - - | | | |
# | | - - - - - - - - - - | | |
# | | | - - - - - - - - - = | |
# | | | | - - - - - - - - = - |
# | | | | | - - - - - - - - - -
# これらはすべて 0 を表すが, このような 0 の表現方法は 6 個 (5 + 1) あるため,
# 全体から 6 を引き,
# C(15, 5) - 6 が 5 桁以下の減少数となる.
#
# 11, 333, 7777 などのすべて同じ数字となる数は,
# 増加数でも減少数でもあるため取り除く.
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, ...)
#
# このような数は n 桁の中に 9n 個存在する.
# 0 は減少数でしか数えていないため考慮しなくてもよい.
#
# よって n 桁以下の増加数または減少数の個数は
#
# 増加数の個数 + 減少数の個数 - 9n である.
#
# 2桁以下の増加数(54個)
#  1,  2,  3,  4,  5,
#  6,  7,  8,  9, 11,
# 12, 13, 14, 15, 16,
# 17, 18, 19, 22, 23,
# 24, 25, 26, 27, 28,
# 29, 33, 34, 35, 36,
# 37, 38, 39, 44, 45,
# 46, 47, 48, 49, 55,
# 56, 57, 58, 59, 66,
# 67, 68, 69, 77, 78,
# 79, 88, 89, 99

# 2桁以下の減少数(63個)
# 99, 98, 97, 96, 95,
# 94, 93, 92, 91, 90,
# 88, 87, 86, 85, 84,
# 83, 82, 81, 80, 77,
# 76, 75, 74, 73, 72,
# 71, 70, 66, 65, 64,
# 63, 62, 61, 60, 55,
# 54, 53, 52, 51, 50,
# 44, 43, 42, 41, 40,
# 33, 32, 31, 30, 22,
# 21, 20, 11, 10,  9,
#  8,  7,  6,  5,  4,
#  3,  2,  1


def C(n, m):
    if m == 0:
        return 1
    else:
        return C(n, m - 1) * (n - m + 1) // m


def num_increase_number(n):
    return C(n + 9, 9) - 1


def num_decrease_number(n):
    return C(n + 10, 10) - (n + 1)


def main():
    n = 100
    return num_increase_number(n) + num_decrease_number(n) - (9 * n)


if __name__ == '__main__':
    print(main())