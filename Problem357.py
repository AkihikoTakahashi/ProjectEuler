# coding: utf-8

# Tips: 解の候補 N は以下の特徴を持つ.
#       2は明らかに題意を満たす
#       N + 1 は素数
#       N / 2 は奇数
#       N は平方因子を持たない N = ab^2 => b + N/b = b + ab = b(1+b)


def is_prime(n):
    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(int(n**0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return primes


def gen_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i


def main():
    lim = 100000000
    is_primes = is_prime(lim + 1)
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
