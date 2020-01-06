# coding: utf-8

# 1, 2, 3, ... 20 の最小公倍数を求めればよい.
# LCD(1, 2, 3, ..., 20) = LCD(LCD(1, 2), 3, 4, ..., 20)
# LCD(a, b) = a * b / GCD(a, b)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def main():
    max_i = 20
    s = 1
    for i in range(1, max_i + 1):
        s = s * i // gcd(s, i)
    return s


if __name__ == "__main__":
    print(main())
