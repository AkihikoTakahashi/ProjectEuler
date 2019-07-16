# coding: utf-8


def main():
    max_i = 100

    return sum([i for i in range(1, max_i + 1)])**2 - sum(
        [i**2 for i in range(1, max_i + 1)])


if __name__ == "__main__":
    print(main())
