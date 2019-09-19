# coding: utf-8

# X を 32 桁の数とする.
# X = ABD は回文数かつ N の倍数とする
# B は 16桁の回文数


# 6桁の回文数は 4桁の回文数を10倍し, 100001(=10**6+1)の倍数を足す
def gen_palindromic(digit, l=0):
    '''digit桁の回文数を生成する'''

    if digit == l:
        yield 0
    elif digit - 1 == l:
        for i in range(10):
            yield i
    else:
        start_i = 1 if l == 0 else 0
        multi = 10**(digit - l - 1) + 1
        for i in range(start_i, 10):
            for palindromic in gen_palindromic(digit, l + 2):
                yield i * multi + 10 * palindromic


def main():
    # def is_palindromic(n):
    #     return str(n) == str(n)[::-1]

    # # N = 10000019
    # # L = 10**32
    N = 109
    L = 10**5

    return sum(pa % N == 0 for i in range(3, 6) for pa in gen_palindromic(i))


if __name__ == '__main__':
    # N = 10000019
    # a = set(i * pow(10, 8, N) % N for i in gen_palindromic(16))
    # print(len(a))
    print(main())
