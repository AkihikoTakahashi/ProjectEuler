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
# n = p * q (p < q) のとき s(n) >= q,
# s(p^e * q^f) = max(s(p^e), s(q^f)) がいえる.
#
# m! % n = 0 ==> (m+1)! % n = 0 である.
#

from itertools import count


def main():
    lim = 10**8
    # lim = 10**2
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
                    smallest[k] = max(j, smallest[i])

                    tmp = j // i
                    while tmp % i == 0:
                        power *= i
                        tmp //= i
    return sum(smallest)
