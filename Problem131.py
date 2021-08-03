# coding: utf-8

# n^3 - n^2 * p = k^3 のとき (p は素数)
# n^3 * ((n + p) / n)^(1/3) = k^3
# よって n + p, n は立方数である.
#
# n = x^3, n + p = y^3 とする.
# p = y^3 - x^3 = (y - x)(x^2 + xy + y^2)
#
# p は素数なので y - x = 1
# y を代入すると p = (x + 1)^3 - x^3 となる.
#
# よって p < 1000000 かつ p は素数となる個数を数える.

from itertools import takewhile, count


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])


def main():
    lim = 1000000
    cnt = 0
    for x in takewhile(lambda x: (x + 1)**3 - x**3 < lim, count(1)):
        p = (x + 1)**3 - x**3
        if is_prime(p):
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
