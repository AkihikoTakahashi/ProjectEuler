# coding: utf-8


def main():
    n = 10**7
    factor_cnts = [2] * (n + 1)

    for i in range(2, n // 2 + 1):
        for ij in range(i * 2, n + 1, i):
            factor_cnts[ij] += 1

    return sum(factor_cnts[i] == factor_cnts[i + 1]
               for i in range(2,
                              len(factor_cnts) - 1))


if __name__ == "__main__":
    print(main())
