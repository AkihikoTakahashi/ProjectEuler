# coding: utf-8

# 20桁の数 N が 11 の倍数となるには
# 偶数桁の和 - 奇数桁の和が 11 の倍数となればよい.
#
from itertools import combinations
from collections import Counter
from math import factorial


def list_difference(list1, list2):
    result = list1.copy()
    for value in list2:
        if value in result:
            result.remove(value)

    return result


def main():

    logs = []
    N = 10
    n_list = sorted([i for i in range(N)] * 2)
    cnt = 0
    for even in combinations(n_list, N):
        odd = list_difference(n_list, even)

        # 偶数桁の和 - 奇数桁の和 が 11 の倍数でなければ 11 の倍数は作れない.
        if (sum(even) - sum(odd)) % 11 != 0:
            continue

        if even in logs:
            continue

        logs.append(even)

        # 偶数桁は先頭が 0 でない順列の作り方を数える.
        counter_even = Counter(even)
        perm_even = 0
        for k, v in counter_even.items():  # 先頭に k を使う
            if k == 0:
                continue
            counter_even[k] -= 1

            f = factorial(N - 1)  # 残り 9 桁の順列の作り方を数える.
            for v2 in counter_even.values():
                f //= factorial(v2)

            perm_even += f
            counter_even[k] += 1

        # 奇数桁は順列の作り方を数える.
        counter_odd = Counter(odd)
        perm_odd = factorial(N)
        for v in counter_odd.values():
            perm_odd //= factorial(v)

        cnt += perm_even * perm_odd
    return cnt


if __name__ == '__main__':
    print(main())
