# coding: utf-8


def sum_digit(n, s=0):
    if 0 <= n <= 9:
        return n + s
    else:
        return sum_digit(n // 10, s + n % 10)


def main():
    n = pow(2, 1000)
    return sum_digit(n)


if __name__ == "__main__":
    print(main())
