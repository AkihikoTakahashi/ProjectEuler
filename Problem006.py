# coding: utf-8


def main():
    n = 100

    pow_of_sum = (n * (n + 1) // 2)**2
    sum_of_pow = n * (n + 1) * (2 * n + 1) // 6

    return pow_of_sum - sum_of_pow


if __name__ == "__main__":
    print(main())
