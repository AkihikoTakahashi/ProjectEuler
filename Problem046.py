# coding: utf-8

# n = p * 2 * q^2  (p: 素数, q: 自然数)
# と書けない <=>
# すべての q (1<=q<=√(n/2)) に対して,
# p = n - 2 * q^2 がすべて合成数.

from itertools import count


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def is_composite(n):
    return n != 1 and not (is_prime(n))


def main():
    return next(
        n for n in count(3, 2) if all(
            is_composite(n - 2 * q**2) for q in range(int((n // 2)**0.5) + 1)))


if __name__ == "__main__":
    print(main())
