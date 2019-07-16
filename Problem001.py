# coding: utf-8


def main():

    lim = 1000
    s = 0
    for i in range(lim):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


if __name__ == '__main__':
    print(main())
