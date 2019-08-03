# coding: utf-8


def concat(n, m):
    def _gen_digit(n):
        nums = []
        while n != 0:
            nums.append(n % 10)
            n //= 10
        return nums

    return n * 10**len(_gen_digit(m)) + m


def is_pandigit(n):

    digit = 0
    count = 0
    tmp = 0
    while n > 0:
        tmp = digit
        digit = digit | 1 << (((n % 10) - 1) % 32)
        if digit == tmp:
            return False
        n //= 10
        count += 1
    return digit == (1 << count) - 1


def main():
    a = 2
    max_a = int((10**9 - 1)**0.5)
    pandigits = []

    while a <= max_a:
        num = a
        i = 1
        while not 10**8 <= num <= 10**9 - 1:
            i += 1
            num = concat(num, a * i)
            if 10**9 <= num:
                break
        if is_pandigit(num):
            pandigits.append(num)
        a += 1
    return max(pandigits)


if __name__ == "__main__":
    print(main())
