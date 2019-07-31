# coding: utf-8


def main():
    m = 10**10
    n = (28433 * pow(2, 7830457, m) + 1) % m

    return n


if __name__ == "__main__":
    print(main())
