# coding: utf-8


def digits(n):
    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    return cnt


def main():
    LIM = 1000
    numerator = 3
    denominator = 2
    cnt = 0

    for _ in range(LIM - 1):
        numerator, denominator = numerator + 2 * denominator, numerator + denominator
        if digits(numerator) > digits(denominator):
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(main())
