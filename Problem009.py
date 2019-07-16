# coding: utf-8

# 1 <= a < b <= 500
# c = 1000 - a - b
# として a**2 + b**2 + c**2 となる (a, b, c) を探す.


def main():
    s = 1000
    for a in range(1, s // 2):
        for b in range(a + 1, s // 2):
            c = s - a - b
            if a**2 + b**2 == c**2:
                return a * b * c


if __name__ == "__main__":
    print(main())
