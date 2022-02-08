# coding: utf-8

# n = 2k + 1 とすると n^2 + 1 は偶数となるので n^2 + 1 が素数となるためには
# n は偶数である必要がある.
# 同様に n = 5k + r (r = 1, 2, 3, 4) とすると n^2 + 9 または n^2 + 1 が 5 の
# 倍数となるため, n は 5 の倍数である必要がある.
# よって n は 10 の倍数である必要がある.
#
# 任意の n に対し, n^2 = 0 または 1 (mod 3) であるが, n^2 = 0 mod 3 のとき
# n^2 + 3 は 3 の倍数となるので n^2 = 1 (mod 3) である必要がある.
# 同様に, n^2 = 2 (mod 7) である必要がある.
#
# これらの条件から, n^2 + 11, n^2 + 17, n^2 + 23 は 3 の倍数, n^2 + 5 は
# 5 の倍数, n^2 + 19 は 7 の倍数であるため, これらが素数でないことを確かめ
# なくてもよい. (n^2 + 21 が素数でないことを確かめれば十分)
#
# 予め小さめの素数 p に対して, n^2 + k mod p (k = 1, 3, 7, 9, 13, 27) が
# 0 にならないような n のリストを p ごとに作っておき, n がすべてのリストに
# 含まれていることを最初にチェックすることで, 素数判定の回数を減らしている.

from itertools import takewhile


def eratosthenes(n):
    ''' Returns  a list of primes < n '''
    primes = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            primes[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if primes[i]]


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


# n**2 + k == 0 mod p か調べる (k = 1, 3, 7, 9, 13, 27)
def check_n(p, increments):
    rets = []
    for n in range(p):
        n2 = n**2
        if all((n2 + inc) % p != 0 for inc in increments):
            rets.append(n)
    return rets


def main():
    n = 150000000
    small_primes = eratosthenes(10000)
    increments = [1, 3, 7, 9, 13, 27]
    mod_check = {p: check_n(p, increments) for p in small_primes}
    ans = 0
    for i in range(10, n, 10):
        if not all(i % p in mod_check[p]
                   for p in takewhile(lambda p: p < i**2, small_primes)):
            continue
        s = i**2
        if is_prime(s +
                    1) and is_prime(s + 3) and is_prime(s + 7) and is_prime(
                        s + 9) and is_prime(s + 13) and is_prime(s + 27) and (
                            not is_prime(s + 21)):
            ans += i

    return ans


if __name__ == '__main__':
    print(main())
