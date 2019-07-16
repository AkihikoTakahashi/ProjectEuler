# coding: utf-8

# R(n) = (10^n - 1) / 9
#
# R(n) = 0 mod p となる素数 p を探す.
# (10^n - 1) / 9 = 0 mod p
# 10^n - 1 = 0 mod 9p
# 10^n = 1 mod 9p
#
# よって n = 10^9 のとき,
# 10^(10^9) = 1 mod 9p なる素数 p を小さいほうから探す.


def gen_prime():
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0:
            return False
        else:
            return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])

    i = 3
    yield 2

    while True:
        if is_prime(i):
            yield i
        i += 2


def main():
    n = 10**9
    gen_primes = gen_prime()
    cnt = 0
    cnt_max = 40
    s = 0
    while cnt < cnt_max:
        p = next(gen_primes)
        if pow(10, n, 9 * p) == 1:
            s += p
            cnt += 1
    return s


if __name__ == "__main__":
    print(main())
