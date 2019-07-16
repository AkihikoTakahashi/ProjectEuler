# coding: utf-8


def is_bouncy(num):
    inc = False
    dec = False

    d_1 = num % 10
    num //= 10

    while num > 0:
        d_10 = num % 10

        if d_10 < d_1:
            inc = True
        elif d_10 > d_1:
            dec = True

        num //= 10
        d_1 = d_10

        if dec and inc:
            return True

    return dec and inc


def main():
    bouncy_cnt = 0
    n = 100
    per = 99

    while bouncy_cnt * 100 < n * per:
        n += 1
        if is_bouncy(n):
            bouncy_cnt += 1

    return n


if __name__ == "__main__":
    print(main())
