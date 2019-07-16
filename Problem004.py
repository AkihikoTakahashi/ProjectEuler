# coding: utf-8


def is_palindromic(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def main():
    return max([
        a * b for a in range(100, 1000) for b in range(100, 1000)
        if is_palindromic(a * b)
    ])


if __name__ == "__main__":
    print(main())
