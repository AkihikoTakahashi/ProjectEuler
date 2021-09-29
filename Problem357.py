# coding: utf-8

# Tips: 解の候補 N は以下の特徴を持つ.
#       2は明らかに題意を満たす
#       N + 1 は素数
#       N / 2 は奇数
#       N は平方因子を持たない N = ab^2 => b + N/b = b + ab = b(1+b)


def eratosthenes(n):
    ''' Returns  a list of primes < n '''
    primes = [False, False] + [True] * (n - 2)
    primes[4::2] = [False] * ((n + 1) // 2 - 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if primes[i]:
            primes[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return primes


def gen_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i


def main():
    lim = 100000000
    is_primes = eratosthenes(lim + 2)
    s = 0

    for n in range(1, lim + 1):

        # n+1 が素数でなければ解の候補ではない
        if not is_primes[n + 1]:
            continue

        for d in gen_divisor(n):

            # 問題の条件を満たすか
            if not is_primes[d + n // d]:
                break
        else:
            s += n
    return s


if __name__ == "__main__":
    print(main())
