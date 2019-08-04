# coding: utf-8

# n = x(x+1)/2 を x で解くと
# x = (-1 + √(8n + 1))/2
# より n が三角数なら (-1 + √(8n + 1))/2 が自然数となる.
# また Problem044.py より
# n = x(3x - 1) / 2 (n, x は自然数) のとき,
# x = (1 + √(1+24n))/6
# より n が五角数なら (1 + √(1+24n))/6 は自然数となる.

from itertools import count


def is_triangle(n):
    return (-1 + (8 * n + 1)**0.5) % 2 == 0


def is_pentagonal(n):
    return (1 + (24 * n + 1)**0.5) % 6 == 0


def main():
    for i in count(144):
        h = i * (2 * i - 1)
        if is_triangle(h) and is_pentagonal(h):
            break
    return h


if __name__ == "__main__":
    print(main())
