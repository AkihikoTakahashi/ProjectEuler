# coding: utf-8

from itertools import count


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])


def next_diag():
    for i in count(3, 2):
        n = i**2
        yield n - (i - 1) * 3, n - (i - 1) * 2, n - (i - 1)


def main():
    cnt = 0
    n = 1
    LIM = 0.1
    for i, d in enumerate(next_diag(), start=1):
        n += 4
        cnt += sum(map(is_prime, d))

        if cnt / n < LIM:
            break

    return 2 * i + 1


if __name__ == '__main__':
    print(main())
