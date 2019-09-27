# coding: utf-8


def gen_palindromic(digit, l=0):
    '''digit桁の回文数を生成する'''

    if digit == l:
        yield 0
    elif digit - 1 == l:
        for i in range(10):
            yield i
    else:
        # start_i = 1 if l == 0 else 0
        start_i = 0
        multi = 10**(digit - l - 1) + 1
        for i in range(start_i, 10):
            for palindromic in gen_palindromic(digit, l + 2):
                yield i * multi + 10 * palindromic


def rev(n):
    rev_n = 0
    while n > 0:
        rev_n = rev_n * 10 + n % 10
        n //= 10
    return rev_n


# 4 の倍数 + 1 ... 123454321 (9) -> 123*10^6 + 454*10^3 + 321
# 4 の倍数 + 2 ... 1234554321 (10) -> 123*10^7 + 4554*10^3 + 321
# 4 の倍数 + 3 ... 12345654321 (11) -> 123*10^8 + 45654*10^3 + 321
# 4 の倍数 ....... 123456654321 (12) -> 123*10^9 + 456654*10^3 + 321
def count_ans(digits, N=10000019):
    from math import ceil
    from collections import Counter

    d = ceil(digits / 4)

    pal_d = digits - 2 * d
    inners = Counter(i * pow(10, d, N) % N for i in gen_palindromic(pal_d))
    outers = Counter((i * pow(10, pal_d + d, N) + rev(i)) % N
                     for i in range(10**(d - 1), 10**d))

    return sum(outers[N - k] * v for k, v in inners.items())


def main():
    N = 10000019
    L = 32

    cnt = 0
    for i in range(8, L + 1):
        _cnt = count_ans(i, N)
        cnt += _cnt
        print(i, _cnt)
    # return sum(count_ans(i, N) for i in range(8, L + 1))
    return cnt


if __name__ == '__main__':
    # N = 10000019
    # a = set(i * pow(10, 8, N) % N for i in gen_palindromic(16))
    # print(len(a))

    print(main())
