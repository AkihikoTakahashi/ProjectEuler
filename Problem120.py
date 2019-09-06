# coding: utf-8

# (a-1)^n = (-1)^n + n * a * (-1)^(n-1) mod a^2
#           = 1 - n * a (n: 偶数)
#             n * a - 1 (n: 奇数)
# (a+1)^n = 1 + n * a
# よって (a - 1) ^ n + (a + 1) ^ n
#        = 2 (n: 偶数)
#          2 * n * a mod a^2 (n: 奇数)
# n = 1 のとき 2 * a mod a^2 > 2 より
# r_max = max(2 * n * a mod a^2)
#   ※ a = 2 のとき, 2 * a mod a^2 = 0 であるが r_max = 0 である
#
# 考える n は n = a のとき 2 * n * a = 0 mod a^2 なので,
# 0 <= n <= a - 1


def calc(a):
    return max(2 * n * a % a**2 for n in range(a))


def main():
    return sum(calc(i) for i in range(3, 1001))


if __name__ == "__main__":
    print(main())
