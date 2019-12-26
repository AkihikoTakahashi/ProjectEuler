# coding: utf-8

# 8桁, 9桁の pandigit 数は素数にならない.
# 8桁の pandigit 数は各桁の和が 36 であり, 必ず 9 の倍数となる.
# 9桁も同様.
# よって 7 桁の最大の pandigit 数 7654321 から探す.


def is_pandigit(n):

    digit = 0
    count = 0
    tmp = 0
    while n > 0:
        tmp = digit
        digit = digit | 1 << (((n % 10) - 1) % 32)
        if digit == tmp:
            return False
        n //= 10
        count += 1
    return digit == (1 << count) - 1


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    return n % 2 != 0 and all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def main():
    max_n = 7654321
    return next(n for n in range(max_n, 2, -1)
                if is_pandigit(n) and is_prime(n))


if __name__ == '__main__':
    print(main())
