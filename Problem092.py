# coding: utf-8

# 9999999 -> 567 より n <= 567 なら結果をメモしてメモの探索範囲を狭める.


def memo(func):
    check = {}

    def f(*args):
        if not args in check:
            ret = func(*args)
            if args[0] <= 567:
                check[args] = ret
        else:
            ret = check[args]
        return ret

    return f


def next_n(n):
    def _gen_digit(n):
        while n != 0:
            yield n % 10
            n //= 10

    return sum(k**2 for k in _gen_digit(n))


@memo
def is_arrive_89(n):
    if n == 1:
        return False
    elif n == 89:
        return True
    return is_arrive_89(next_n(n))


def main():
    N = 10**7
    return sum(is_arrive_89(i) for i in range(1, N + 1))


if __name__ == "__main__":
    print(main())
