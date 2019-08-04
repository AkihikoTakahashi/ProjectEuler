# coding: utf-8

# n = x(3x - 1) / 2 (n, x は自然数) のとき,
# 3x^2 - x - 2n = 0 より, x = (1 + √(1+24n))/6 と書ける.
# よって n が五角数なら (1 + √(1+24n))/6 は自然数となる.


def is_pentagonal(n):
    return (1 + (1 + 24 * n)**0.5) % 6 == 0


def main():
    i = 2
    while True:
        p1 = i * (3 * i - 1) // 2

        for j in range(i - 1, 1, -1):
            p2 = j * (3 * j - 1) // 2
            if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
                ans = p1 - p2
                break

        else:
            i += 1
            continue
        break
    return ans


if __name__ == "__main__":
    print(main())
