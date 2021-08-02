# coding: utf-8

# R(n) = (10^n - 1) / 9 とする.
# R(10^n) = (10^(10^n) - 1) / 9 が 素数 p の倍数になるような
# n があるか調べる.
#
# 明かに p = 2, 3, 5 のとき R(n) が p に倍数になり得ない.
#
# R(10^n) = (10^(10^n) - 1) * 9^-1 mod p = 0
# となるとき 9^-1 は p と互いに素なので 10^(10^n) - 1 は p の倍数である.
# d を 10^d = 1 mod p となる最小の整数とする. (d は p - 1 の約数である)
#
# 10^n が d の倍数となるとき,
# 10^(10^n) = 10^(d*X) = (10^d)^X = 1^X = 1 mod p となる
# R(10^n) は p の倍数となる n が存在する.
# また 10^n が d の倍数となるには d = 2^a * 5^b である.
#
# よって 10^d = 1 mod p なる d に対し, d = 2^a * 5^b のとき
# R(n) は p の倍数になるような n が存在する.
#


def eratosthenes(n):
    '''n 以下の素数を返す'''
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes


def gen_factor(n):
    ''' n の約数を生成する'''
    large_divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


def get_ind(a, p):
    '''a^x = 1 mod p なる x を返す'''

    for d in gen_factor(p - 1):
        if pow(a, d, p) == 1:
            return d
    return None


def main():
    N = 100000

    primes = [i for i, p in enumerate(eratosthenes(N)) if p]
    primes = primes[3:]  # 解が明らかな p = 2, 3, 5 を除外

    s = 2 + 3 + 5
    for p in primes:
        d = get_ind(10, p)
        if d is None:
            continue
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        if d != 1:
            s += p
    return s


if __name__ == '__main__':
    print(main())
