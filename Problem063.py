# coding: utf-8

# n-1 <= n * log10(9) <= n
# は 1 <= n <= 22 で満たす.
# よって 22 乗数までを探せばよい.


def digit(n):
    d = 0

    while n != 0:
        d += 1
        n //= 10
    return d


def main():
    lim = 22
    return len(
        set(base**i for i in range(1, lim + 1) for base in range(1, 10)
            if i == digit(base**i)))


if __name__ == "__main__":
    print(main())
