# coding: utf-8

# D 桁の数を XYZW に分割し, 10000019 の倍数とする
# X, W はそれぞれ D/4 桁 (小数点切り上げ)で, rev(X) = W
# YZ は回文数で, (D - (X, Z の桁数の和))桁である.

# D 桁の数の外側だけを抜き出した数 X0...0W と, 内側だけを抜き出した数
# YZ0...0 について考える.
# 元の数は外側の数 + 内側の数であり, 10000019 で割ると 0 になる.
# よって X0...0W + YZ0...0 % 10000019 = 0


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


def count_ans(digits, N):
    from math import ceil
    from collections import Counter

    d = ceil(digits / 4)

    pal_d = digits - 2 * d
    inners = Counter(i * pow(10, d, N) % N for i in gen_palindromic(pal_d))
    outers = Counter((i * pow(10, pal_d + d, N) + rev(i)) % N
                     for i in range(10**(d - 1), 10**d))

    return sum(outers[(N - k) % N] * v for k, v in inners.items())


def main():
    N = 10000019
    L = 32

    return sum(count_ans(i, N) for i in range(3, L + 1))


if __name__ == '__main__':
    print(main())
