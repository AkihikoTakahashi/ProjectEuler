# coding: utf-8

# n = a*b (a < b) としてa, b, n を連結した数 abn が 9桁の pandigit か判定する.
# abn が 9桁であるためには n は4桁である必要がある.
# n が 5桁なら a の桁と b の桁の和は 5 または 6 となり, abn は 9桁を越える.
# n が 3桁なら a の桁と b の桁の和は 3 または 4 となり, abn は 8桁以下となる.
# n が 4桁なら a の桁と b の桁の和は 4 または 5 となり, 各桁の和が 5 のとき
# abn は pandigit な 9桁の数となり得る.


def is_pandigit(n):

    digit = 0
    count = 0
    tmp = 0
    while n > 0:
        tmp = digit
        digit = digit | 1 << ((n % 10 - 1) % 32)
        if digit == tmp:
            return False
        n //= 10
        count += 1
    return digit == (1 << count) - 1


def main():

    min_i = 1000
    max_i = 9999
    sum_pandigit = 0

    for i in range(min_i, max_i + 1):
        divisors = ([a, i // a] for a in range(2,
                                               int(i**0.5) + 1) if i % a == 0)

        for p, q in divisors:
            concat = int(str(p) + str(q) + str(p * q))
            if 10**8 <= concat <= 10**9 - 1 and is_pandigit(concat):
                sum_pandigit += i
                break

    return sum_pandigit


if __name__ == "__main__":
    print(main())
