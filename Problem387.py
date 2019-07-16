# coding: utf-8

# 1桁の数はすべて harshad である.
# n桁のすべての harshad 数の集合を H_n として
# n+1桁の 右側 harshad 数は H_n+1 = 10*a+i (a は H_n の要素, 0 <= i <= 9)
# の形で書ける.
#
# 15桁の整数であれば通常の素数判定法が使える.
#


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])


def sum_digit(n, s=0):
    if 0 <= n <= 9:
        return s + n
    else:
        return sum_digit(n // 10, s + (n % 10))


def is_harshad(n):
    return n % sum_digit(n) == 0


def make_right_harshad(digit, n=1, harshads=[]):
    """ digit 桁以下の harshad 数リストを作成する. """
    if digit < n:
        return harshads

    if n == 1:
        return make_right_harshad(digit, n + 1,
                                  harshads + [1, 2, 3, 4, 5, 6, 7, 8, 9])

    else:
        new_harshads = []
        for h in harshads:
            if 10**(n - 2) <= h <= 10**(n - 1):
                for i in range(0, 10):
                    if is_harshad(10 * h + i):
                        new_harshads.append(10 * h + i)
        return make_right_harshad(digit, n + 1, harshads + new_harshads)


# 引数には harshad 数を渡すので強いかどうかを判定する.
def is_strong_right_harshad(harshad):
    return is_prime(harshad // sum_digit(harshad))


def main():
    digit = 14

    # 14桁以下の強い harshad 素数を探すので 13桁以下の harshad 数を探す
    right_harshad = make_right_harshad(digit - 1)

    strong_right_harshad = [
        h for h in right_harshad if is_strong_right_harshad(h)
    ]

    strong_right_harshad_primes = [
        10 * s_r_harshad + i for s_r_harshad in strong_right_harshad
        for i in [1, 3, 7, 9] if is_prime(10 * s_r_harshad + i)
    ]

    return sum(strong_right_harshad_primes)


if __name__ == "__main__":
    print(main())
