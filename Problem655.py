# coding: utf-8


def gen_palindrom(palindroms, stop_digit=32):
    def digit(n):
        d = 0
        while n != 0:
            d += 1
            n //= 10
        return d

    while True:
        new_palindroms = []
        for palindrom in palindroms:

            d = digit(palindrom)
            for i in range(1, 10):
                new_palindrom = i * (10**(d + 1) + 1) + 10 * palindrom
                yield new_palindrom
                new_palindroms.append(new_palindrom)

        if d + 2 > stop_digit:
            break

        palindroms = new_palindroms


def main():
    for i in gen_palindrom(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]):
        if i % 109 == 0:
            print(i)
