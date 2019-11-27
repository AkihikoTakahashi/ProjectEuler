# coding: utf-8

from itertools import takewhile, count


def is_palindromic(n):
    str_n = str(n)
    return str_n[::-1] == str_n


# a^2 + (a+1)^2 < n
# max(a) = sqrt(n/2)
# m^2 + ... + n^2 = n(n+1)(2n+1)/6 - (m-1)m(2m-1)/6
def gen_consective_square(n):
    '''n以下の連続する2乗和を生成'''

    max_m = int((n / 2)**0.5)
    for m in range(1, max_m):
        for consective_sq_sum in takewhile(lambda t: t < n,
                                           (e * (e + 1) * (2 * e + 1) // 6 -
                                            (m - 1) * m * (2 * m - 1) // 6
                                            for e in count(m + 1))):
            yield consective_sq_sum


def main():
    N = 10**8
    s = set(n for n in gen_consective_square(N) if is_palindromic(n))

    return sum(s)


if __name__ == "__main__":
    print(main())
