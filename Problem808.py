# coding: utf-8

# 素数 p の 2 乗の 1 の位は 1 または 9 である.
# n が Reversible prime squares のとき rev(n) も
# Reversible prime squares なので, 検索対象は 先頭桁が 1 のみの数でよい.

from itertools import count

def range2():
    for i in count(0, 10):
        yield i + 1
        yield i + 3
        yield i + 7
        yield i + 9


def is_square(n):
    if n < 0:
        return False

    return n == int(n**0.5) ** 2


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def eratosthenes(n):
    '''Returns  a list of primes < n'''
    primes = [False, False] + [True] * (n - 2)
    primes[4::2] = [False] * ((n + 1) // 2 - 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            primes[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return primes


def main():
    N = 50
    primes = eratosthenes(100000000)
    cnt = 0
    s = 0
    for n, n2 in ((i, i**2) for i in range2()):
        if not primes[n]:
            continue
        if is_palindrome(n2):
            continue
        n2_rev = int(str(n2)[::-1])
        if not is_square(n2_rev):
            continue
        if primes[int(n2_rev**0.5)]:
            cnt += 1
            s += n2
            if cnt == N:
                break
    return s


if __name__ == '__main__':
    print(main())
