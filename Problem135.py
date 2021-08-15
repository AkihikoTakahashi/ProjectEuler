# coding: utf-8

# 公差 d, 等差数列のなかで最も小さい項を z とすると
# x = z + 2d, y = z + d
#
# x^2 - y^2 - z^2 = n
# (z + 2d)^2 - (z + d)^2 - z^2 = n
# 整理すると
# (3d - z)(d + z) = n
#
# 3d - z = u, d + z = v とする. (u, v > 0)
# uv = n, d = (u + v) / 4, z = (-u + 3v) / 4
#
# よって uv < 1000000 の u, v に対して,
# u + v = 0 mod 4, -u + 3v = 0 mod 4, u < 3v なら
# ans[uv] を 1 増やす.
# u + v = 0 mod 4 のとき v = -u mod 4 で, -u + 3v = 4v = 0
# なので u + v = 0 mod 4 のとき -u + 3v = 0 mod 4 も満す.
#
# u + v = 0 mod 4 より v = 4 - (u % 4) + 4k
# u / 3 < v より u / 3 < 4 - (u % 4) + 4k
# k > u / 12 - 1 + (u % 4) / 4
# から k = int(u / 12 - 1 + (u % 4) / 4)
# として, v0 = 4 - (u % 4) + 4 * k
# を v の初期値とすると無駄なループが削減される.

from itertools import takewhile


def main():
    N = 1000000
    ans = [0] * N

    for u in range(1, N):
        # u % 4 == 4 - v % 4 かつ, v > u/3 となる最小の v = v0
        # を求める.
        k = int(u / 12 - 1 + (u % 4) / 4)
        v0 = 4 - (u % 4) + 4 * k
        for v in takewhile(lambda v: u * v < N, range(v0, N, 4)):
            if -u + 3 * v > 0:
                n = u * v
                ans[n] += 1

    return sum(1 for _ in filter(lambda i: i == 10, ans))


if __name__ == '__main__':
    print(main())
