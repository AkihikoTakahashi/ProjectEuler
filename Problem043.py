# coding: utf-8

# 1406357289
# d[i] (0<=i<10) を 0 から 9 の数とし, d[i]d[i+1]d[i+2] を 3桁の値とする.
# d[1]d[2]d[3] は 2 の倍数なので d[3] は偶数.
# d[2]d[3]d[4] は 3 の倍数なので d[2]+d[3]+d[4] は 3 の倍数.
# d[3]d[4]d[5] は 5 の倍数なので d[5] = 5 の倍数.
# d[5]d[6]d[7] は 11 の倍数なので d[5] - d[6] + d[7] は 11 の倍数.

from itertools import permutations


def main():
    s = 0
    for d in permutations(range(10), 10):
        if d[0] == 0:
            continue
        if d[3] % 2 != 0:
            continue
        if (d[2] + d[3] + d[4]) % 3 != 0:
            continue
        if d[5] % 5 != 0:
            continue
        if (d[5] - d[6] + d[7]) % 11 != 0:
            continue

        n_7 = 100 * d[4] + 10 * d[5] + d[6]
        n_13 = 100 * d[6] + 10 * d[7] + d[8]
        n_17 = 100 * d[7] + 10 * d[8] + d[9]
        if n_7 % 7 == 0 and n_13 % 13 == 0 and n_17 % 17 == 0:
            _s = 0
            for n in d:
                _s = 10 * _s + n
            s += _s
    return s


if __name__ == "__main__":
    print(main())
