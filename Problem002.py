# coding: utf-8


def gen_fibo():
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


def main():
    s = 0
    fibo = gen_fibo()
    lim = 4000000

    for f in fibo:
        if f > lim:
            break

        if f % 2 == 0:
            s += f
    return s


if __name__ == "__main__":
    print(main())
