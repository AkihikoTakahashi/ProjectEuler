# coding: utf-8

# 巡回数は 10^d - 1 が p で割り切れないような
# 素数 p に対して 1/p の上位 p-1 桁で得られる. (1 <= d < p)
# つまり 10 が p の原始根となるとき 1/p は巡回数を生成する.
#
# 左端の 11 桁が 00000000137 なので 0.00000000137 <= 1/p < 0.00000000138
# を満たす.
# すなわち p の範囲は 1/0.00000000138 < p <= 1/0.00000000137 である.
#
# 素数 p の逆数 1/p から生成された巡回数に p を掛けると 9 が p-1 個並ぶ.
# よって右端の 56789 に p を掛けると 99999 となるような p, すなわち,
# p = 99999 * 56789^-1 = -1 * 56789^-1 mod 100000 に絞られる.
#
# 1/p + (p-1)/p = 0.9999... のように 9 が p-1 個続くことから,
# 巡回数の各桁の和は 9(p - 1)/2 で求まる.

from itertools import takewhile, dropwhile, count, islice


def nth(n, iterable, default=None):
    return next(islice(iterable, n, None), default)


# 10^d  % p == 1 (1 <= d < p) かどうか
def is_divide(p):
    x = 1
    for _ in range(1, (p + 1) // 2):
        x *= 10
        x %= p
        if x == 1:
            return False
    return True


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in takewhile(lambda i: i * i < n, count(3, 2)))


def is_primitive_root(a, p):
    '''a は p の原始根か判定する'''

    n = p - 1
    factors = []
    i = 2
    while n != 1:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1

    return all(pow(a, (p - 1) // fac, p) != 1 for fac in factors)


def main():
    min_n = int(1 / 0.00000000138)
    max_n = int(1 / 0.00000000137)

    inv = pow(56789, 100000 - 1, 100000)
    right_num = (-1 * inv) % 100000
    p = nth(0, [
        i for i in range(min_n, max_n + 1) if i %
        100000 == right_num and is_prime(i) and is_primitive_root(10, i)
    ])

    sum_digit = 9 * (p - 1) // 2

    return sum_digit


if __name__ == '__main__':
    print(main())
