# coding: utf-8

from itertools import permutations, product, count, takewhile


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    funcs = [add, minus, mul, div]

    max_consective = 0

    for a, b, c, d in permutations(range(1, 10), 4):
        s = set()
        for x, y, z, w in permutations([a, b, c, d], 4):
            for f1, f2, f3 in product(funcs, repeat=3):
                r = f3(f2(f1(x, y), z), w)
                if r > 0 and r * 10 // 10 == r:
                    s.add(int(r))
            for f1, f2, f3 in product(funcs, repeat=3):
                r = f3(f1(x, y), f2(z, w))
                if r > 0 and r * 10 // 10 == r:
                    s.add(int(r))

        consective = len([i for i in takewhile(lambda i: i in s, count(1))])
        if consective > max_consective:
            ans = sorted([x, y, z, w])
            max_consective = consective

    return ''.join(map(str, ans))


if __name__ == '__main__':
    print(main())
