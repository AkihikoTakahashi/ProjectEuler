# coding: utf-8

from itertools import count, takewhile


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])


def A(n):
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if _gcd(n, 10) != 1:
        return 0

    x = 1
    k = 1

    while x != 0:
        x = (10 * x + 1) % n
        k += 1
    return k


def main():
    cnt_lim = 25
    cnt = 0
    s = 0
    for n in takewhile(lambda: cnt < cnt_lim, count(3)):
        # for n in count(3):
        if is_prime(n):
            continue

        a_n = A(n)
        if a_n != 0 and (n - 1) % a_n == 0:
            cnt += 1
            s += n
        if cnt == cnt_lim:
            break
    return s


if __name__ == '__main__':
    print(main())
