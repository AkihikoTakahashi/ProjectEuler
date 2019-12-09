# coding: utf-8

#
# Collatz(n) は同じ n に対して何度も計算されるのでメモ化する.
#
# Collatz(3) を処理すると, 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# であり Collatz(3) = 8 であるが, 同時に Collatz(10) = 7, Collatz(5) = 6
# なども求まる.
#
# また Collatz(6) は 6 -> 3 -> 10 -> ... -> 1 の順に処理されるが,
# Collatz(3) = 8 がすでに分かっているので, Collatz(6) = 1 + Collatz(3) = 9
# がただちに求まる.
#


def memorize(f):

    table = dict()

    def func(n, c=0):
        if n not in table:
            table[n] = f(n)
        return c + table[n]

    return func


@memorize
def Collatz(n, cnt=0):
    if n == 1:
        return cnt + 1
    else:
        if n % 2 == 0:
            return Collatz(n // 2, cnt + 1)
        else:
            return Collatz(3 * n + 1, cnt + 1)


def main():
    longest = 0
    max_i = 1000000
    for i in range(1, max_i + 1):
        length = Collatz(i)

        if longest < length:
            longest_i = i
            longest = length

    return longest_i


if __name__ == "__main__":
    print(main())
