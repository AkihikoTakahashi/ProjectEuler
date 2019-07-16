# coding: utf-8


def is_amicable(n):
    def _get_divisors(n):
        from functools import reduce
        divisors = list(
            set(
                reduce(list.__add__,
                       [[i, n // i]
                        for i in range(1,
                                       int(n**0.5) + 1) if n % i == 0])))

        divisors.remove(n)
        return divisors

    m = sum(_get_divisors(n))
    return n != m and n == sum(_get_divisors(m))


def main():
    max_i = 10000
    return sum([i for i in range(2, max_i + 1) if is_amicable(i)])


if __name__ == "__main__":
    print(main())
