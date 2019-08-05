# coding: utf-8

# 既約分数 p/q のすぐ左にある既約分数を n/d とする.
# このとき n * q = d * p - 1 が成り立つ. これを変形して,
# n = (d * p - 1) / q である.


def main():
    d = 1000000
    p, q = 3, 7

    while not (d * p - 1) % q == 0:
        d -= 1
    n = (d * p - 1) // q

    return n


if __name__ == "__main__":
    print(main())
