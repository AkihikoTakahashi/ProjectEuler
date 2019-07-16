# coding: utf-8

# 999999 < 6 * 9! = 2177280,
# 9999999 > 7 * 9! = 2540160 より 2540160 を上限としてよい

from math import factorial


def main():
    lim = 2540160
    s = 0
    for i in range(3, lim):
        if i == sum(factorial(int(x)) for x in str(i)):
            s += i

    return s


if __name__ == "__main__":
    print(main())
