# coding: utf-8


def Combination(n, r):
    from math import factorial
    return factorial(n) // (factorial(n - r) * factorial(r))


def main():
    x, y = 20, 20
    return Combination(x + y, x)


if __name__ == "__main__":
    print(main())
