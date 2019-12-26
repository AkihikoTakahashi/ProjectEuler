# coding: utf-8


def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def main():
    n = pow(2, 1000)
    return sum_digit(n)


if __name__ == "__main__":
    print(main())
