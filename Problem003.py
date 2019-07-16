# coding: utf-8


def main():
    n = 600851475143
    p = 2

    while n != 1:
        while n % p == 0:
            n //= p
        p += 1

    return p - 1


if __name__ == "__main__":
    print(main())
