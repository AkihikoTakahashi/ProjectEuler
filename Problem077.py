# coding: utf-8

# ways[k] に k を素数で分割する方法の個数を格納する.
# ways[k] = ways[k-2] + ways[k-3] + ways[k-5] + ... ways[k-p] である.
# ただし p は k を超えない最大の素数.


def eratosthenes(n):
    '''n 以下の素数を返す'''
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]


def main():
    target = 5  # 素数の和に分割できる最小の素数
    primes = eratosthenes(100)  # use magic number 100
    lim = 5000

    while True:
        ways = [0] * (target + 1)
        ways[0] = 1

        for prime in primes:
            for j in range(prime, target + 1):
                ways[j] += ways[j - prime]
        if ways[-1] >= lim:
            break

        target += 1

    return target


if __name__ == '__main__':
    print(main())
