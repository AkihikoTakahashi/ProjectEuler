# coding: utf-8


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def main():
    return max(
        digit_sum(pow(a, b)) for a in range(1, 100) for b in range(1, 100))


if __name__ == '__main__':
    print(main())
