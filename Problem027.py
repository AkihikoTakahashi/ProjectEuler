# coding: utf-8

# f(n) = n^2 + a*n + b とする.
# f(0) = b より b は素数.
#
# b = 2 とすると f(1) = 3+a より a は偶数となり, f(2) も偶数となる
# ので b = 2 も除外できる. よって b は 3 以上の奇数と言える.
#
# a は偶数とすると, f(1) = 1 + a + b より, f(1) は偶数となるので
# a は奇数と言える.

from functools import lru_cache


@lru_cache(maxsize=1024)
def is_prime(p):
    if p <= 1:
        return False
    elif p <= 3:
        return True
    elif p % 2 == 0:
        return False

    return all([p % i != 0 for i in range(3, int(p**0.5) + 1, 2)])


def main():
    lim_a = 1000
    lim_b = 1000
    max_n = 1
    for a in range(-lim_a + 1, lim_a + 1, 2):
        for b in range(3, lim_b + 1, 2):
            if not is_prime(b):
                continue

            n = 1

            # n=0 は確認済み
            while is_prime(n**2 + a * n + b):
                n += 1
            if max_n < n:
                max_n = n
                a_mul_b = a * b
    return a_mul_b


if __name__ == "__main__":
    print(main())
