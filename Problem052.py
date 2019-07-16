# coding: utf-8


def is_permutate(*numbers):
    def _gen_digit(n):
        digits = []
        while n != 0:
            digits.append(n % 10)
            n //= 10
        return digits

    return all(
        sorted(_gen_digit(numbers[i])) == sorted(_gen_digit(numbers[i + 1]))
        for i in range(len(numbers) - 1))


def main():
    i = 1

    while not is_permutate(i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i):
        i += 1

    return i


if __name__ == "__main__":
    print(main())
