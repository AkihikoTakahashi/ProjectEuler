# coding: utf-8


def rev(n):
    s = 0
    while n > 0:
        s = 10 * s + n % 10
        n //= 10
    return s


def is_palindromic(n):
    str_n = str(n)
    return str_n[::-1] == str_n


def is_lychrel(n, cnt=0):
    if cnt == 50:
        return True

    next_n = n + rev(n)
    if is_palindromic(next_n):
        return False
    else:
        return is_lychrel(next_n, cnt + 1)


def main():
    return sum(is_lychrel(i) for i in range(1, 10000))


if __name__ == "__main__":
    print(main())
