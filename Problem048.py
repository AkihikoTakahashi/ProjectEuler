# coding: utf-8


def main():
    max_i = 1000
    return sum(pow(i, i, 10**10) for i in range(1, max_i + 1)) % 10**10


if __name__ == "__main__":
    print(main())
