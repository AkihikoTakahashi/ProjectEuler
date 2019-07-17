# coding: utf-8

# R(10^1), R(10^2), R(10^3) は 17で割り切れないが R(10^4) は割り切れる
# R(n) = (10^n-1)/9
#
# R(n) が素数 p で割り切れる <=> R(n) = 0 mod p <=>
# (10^n - 1) / 9 = 0 mod p <=> 10^n - 1 = 0 mod 9p <=>
# 10^n = 1 mod 9p
#
# よって,
# R(n) が素数 p で割り切れない <=> 任意の n>=1 に対し, 10^n != 1 mod 9p
#
# 問題文の 17, 41, 73 で確かめると,
# 10^10000 = 1 mod 17
# 10^10 = 1 mod 41
# 10^1000 = 1 mod 73
#
# この方法では1601あたりから全然進まないので手順を変える.
#
# Problem129より gcd(10, k) となる任意の k に対して k で割り切れる R(n)
# が存在する. よって k を任意の素数 p とする. (p != 2, 5)
#
# また, k = am と書けるなら R(a) は R(k) で割り切れる.
#   R(am) = '111...(am)...111' (1 が am 個並ぶ)
#   R(a) = '111...(a)...111' (1 が a 個並ぶ)
#   R(am)/R(a) = '100...(a-1)...000''100...(a-1)...001'1
#   (100...(a-1)...000 が m-1 個並び, 最後に 1 が並ぶ)
#
#   例: k=12, a=4, m=3
#   R(12)/R(4) = 100010001
#
# よって R(10^n) が k で割り切れるには, 10^n が k で割り切れる.


def eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(int(n**0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    p = [i for i in range(n + 1) if primes[i]]
    return p


def main():
    primes = eratosthenes(100000)
    n = 1
    s = 0
    for p in primes:
        check = []
        while True:
            a = pow(10, n, 9 * p)
            if a == 1:
                print(p)
                s += p
                break
            elif a in set(check):
                break
            check.append(a)
            n *= 10


if __name__ == "__main__":
    print(main())
