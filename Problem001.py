# coding: utf-8

# 3 の倍数または 5 の倍数の和は 3 の倍数の和 + 5 の倍数の和 - 15 の倍数の和


def sum_n_multiple(n, L):
    k = L // n
    return (n + (n * k)) * k // 2


def main():

    lim = 1000
    return sum_n_multiple(3, lim - 1) + sum_n_multiple(
        5, lim - 1) - sum_n_multiple(15, lim - 1)


if __name__ == '__main__':
    print(main())
