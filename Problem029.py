# coding: utf-8


def main():
    max_a = 100
    max_b = 100

    return len(
        set(a**b for a in range(2, max_a + 1) for b in range(2, max_b + 1)))


if __name__ == "__main__":
    print(main())
