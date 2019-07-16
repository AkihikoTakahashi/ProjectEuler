# coding: utf-8

# 下の各行の和が等しくなる組合せを探す.
#   A--F--G
#   B--G--H
#   C--H--I
#   D--I--J
#   E--J--F
#
# 連結後は16桁であることから, 10 は A, B, C, D, E のいずれかであり,
# e = 10 としても一般性を失なわない.

from itertools import permutations
from functools import reduce


def is_5_gon(line1, line2, line3, line4, line5):

    return sum(line1) == sum(line2) == sum(line3) == sum(line4) == sum(line5)


def make_5_gon_num(line1, line2, line3, line4, line5):
    lines = [line1, line2, line3, line4, line5]

    # 一番外側が最小のものが先頭にくるように回転させる
    min_idx = lines.index(
        min([line1, line2, line3, line4, line5], key=lambda x: x[0]))
    l_5_gon_num = lines[min_idx:] + lines[:min_idx]

    flatten_5_gon_num = reduce(lambda x, y: x + y, l_5_gon_num)

    return int(reduce(lambda x, y: str(x) + str(y), flatten_5_gon_num))


def main():
    five_gon_nums = list()
    e = 10
    for a, b, c, d, f, g, h, i, j in permutations(range(1, 10), 9):

        line1 = [a, f, g]
        line2 = [b, g, h]
        line3 = [c, h, i]
        line4 = [d, i, j]
        line5 = [e, j, f]

        if is_5_gon(line1, line2, line3, line4, line5):
            five_gon_nums.append(
                make_5_gon_num(line1, line2, line3, line4, line5))

    return max(five_gon_nums)


if __name__ == "__main__":
    print(main())
