# coding: utf-8


def dec2bin(n):
    b = format("{0:b}".format(n))
    return b


def main():
    lim = 1000000
    s = 0
    for i in range(1, lim + 1, 2):
        if str(i) == str(i)[::-1] and dec2bin(i) == dec2bin(i)[::-1]:
            s += i
    return s


if __name__ == "__main__":
    print(main())
