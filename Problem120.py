# coding: utf-8

# f(n) = (a - 1)^n + (a + 1)^n とおく.
#
# (a-1)^n = (-1)^n + n * a * (-1)^(n-1) mod a^2
#           = 1 - n * a (n: 偶数)
#             n * a - 1 (n: 奇数)
# (a+1)^n = 1 + n * a
# よって
# f(n) = 2                 (n: 偶数)
#        2 * n * a mod a^2 (n: 奇数)
# n = 1 のとき 2 * a mod a^2 > 2 より
# r_max = max(2 * n * a mod a^2) と書ける.
#
# (1) a = 0 mod 4 のとき
# n = (a - 2)/ 2 のとき f(n) は最大値となる.
# f(n) = a * (a - 2) mod a^2 となるが,
# f(n) はすべて 2 * a の倍数であり, a * (a - 2) は
# a^2 未満のなかで最大の 2 * a の倍数だからである.
#
# (2) a = 1 mod 4 のとき
# n = (a - 3) / 2 のとき f(n) は最大値となる.
# f(n) = a * (a - 3) mod a^2 となり,
# a^2 未満のなかで最大の 2 * a の倍数である.
#
# 残りも同様に,
#
# (3) a = 2 mod 4 のとき
# n = a - 1 のとき f(n) は最大値 a * (a - 2) を取る.
#
# (4) a = 3 mod 4 のとき
# n = (a - 1) / 2 のとき f(n) は最大値 a * (a - 1) を取る.
#
# (1) から (4) を総括すると, f(n) の最大値 r_max は
# a = 0 mod 2 のとき
#   r_max = a * (a - 2)
# a = 1 mod 4 のとき
#   r_max = a * (a - 3)
# a = 3 mod 4 のとき
#   r_max = a * (a - 1)
# が言える.


def calc(a):
    if a % 2 == 0:
        r_max = a * (a - 2)
    elif a % 4 == 1:
        r_max = a * (a - 3)
    else:
        r_max = a * (a - 1)
    return r_max


def main():
    return sum(calc(i) for i in range(3, 1001))


if __name__ == "__main__":
    print(main())
