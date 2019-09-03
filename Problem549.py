# coding: utf-8

# m! が n で割り切れる最小の m のとき, s(n) = m と書く.
# s(10) = 5, s(25) = 10 である.
# s(1) = 0
# s(2) = 2
# s(3) = 3
# s(4) = 4
# s(5) = 5
# s(6) = 3
# s(7) = 7
# s(8) = 4
# s(9) = 6
# s(10) = 5
# s(11) = 11
# s(12) = 4
# s(2^10) = 12
#   12/2+12/4+12/8 = 10
#
# n (n>=2) に対して 2 <= s(n) <= n である.
# 特に n が素数のときのみ, s(n) = n である.
#
# n = p^e について考える.
# s(n) = m のとき, m は p の倍数である.
# なぜなら m = a * p + r となる自然数 a と r (a >= 1, 0 < r < p) が存在すれば,
# m! と (m-1)! の p の指数は同じである. これは m! が n で割り切れるなら,
# (m-1)! も n で割り切れ, s(n) の最小性に反する.

# n = p * q (p < q, p, q は素数) のとき s(n) >= q,
# s(p^e * q^f) = max(s(p^e), s(q^f)) がいえる.
#
# p = 2 とする.
# j = 1 * p のとき, j! = 2 * 1 より素因数 2 を 1 つ持つ.
#                   すべての 2^1 の倍数に対して素因数 2 を 1 つ以上持つ.
# j = 2 * p のとき, j! = 4! より素因数 2 を 3 つ持つ.
#                   すべての 2^2 の倍数に対して素因数 2 を 3 つ以上持つ.
# j = 3 * p のとき, j! = 6! より素因数 2 を 4 つ持つ.
#                   すべての 2^4 の倍数に対して素因数 2 を 4 つ以上持つ.
# j = 4 * p のとき, j! = 8! より素因数 2 を 7 つ持つ
#                   すべての 2^8 の倍数に対して素因数 2 を 7 つ以上持つ.
# これを j が上限を超えるまで繰り返すと n = k*p に対して s(n) が求まる.
# つぎに p = 3 として, 同様の手順を繰り返す.

from itertools import count


def main():
    # lim = 10**8
    lim = 300
    smallest = [0] * (lim + 1)
    for i in range(2, len(smallest)):
        if smallest[i] == 0:
            # smallest[i] は素数

            power = 1

            for j in count(i, i):
                power *= i

                if power > lim:
                    break

                for k in range(power, len(smallest), power):
                    smallest[k] = max(j, smallest[k])

                tmp = j // i
                while tmp % i == 0:
                    power *= i
                    tmp //= i
                print(smallest)
                print(power)
    print(smallest)

    return sum(smallest)


if __name__ == "__main__":
    print(main())
