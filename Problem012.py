# coding: utf-8


def gen_triangle():
    n = 0
    i = 1
    while True:
        n += i
        yield n
        i += 1


def cnt_factors(n):

    from functools import reduce

    factors = set(
        reduce(list.__add__, [[i, n // i]
                              for i in range(1,
                                             int(n**0.5) + 1) if n % i == 0]))
    return len(factors)


def main():
    d_cnt = 500
    for n in gen_triangle():
        if cnt_factors(n) > d_cnt:
            return n


if __name__ == "__main__":
    print(main())
