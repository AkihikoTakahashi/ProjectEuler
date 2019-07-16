# coding: utf-8


def get_divisors(n):
    from functools import reduce
    divisors = list(
        set(
            reduce(list.__add__,
                   [[i, n // i]
                    for i in range(1,
                                   int(n**0.5) + 1) if n % i == 0])))
    del divisors[divisors.index(n)]

    return divisors


def main():
    def _count_chain(n, cnt=0, log=[]):
        if log != [] and n == log[0]:
            return cnt
        elif n in [0, 1] or n > limit or n in log:
            return 0
        else:
            return _count_chain(divisors[n], cnt + 1, log + [n])

    limit = 1000000
    divisors = [0] + [sum(get_divisors(i)) for i in range(1, limit)]

    chains = [_count_chain(i) for i in range(limit)]
    return chains.index(max(chains))


if __name__ == "__main__":
    print(main())
