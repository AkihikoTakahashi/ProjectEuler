# coding: utf-8

# g(N) = 3N とする
# 次の N は N = N + k + 1 ただし, gcd(3N + k, N + k + 1) = 2k + 3, 0 <= k < N - 1
#
# これを実行するため, 以下の手順を行う
#
# g(N) = 3N とする
# 2N - 1 の最小の素因数を調べる 2N - 1 = p1^e1 * p2^e2 * ... * pn^en の場合 p1
# 2k + 3 = p1 を k で解く
# 次の N は N = n + k + 1 となる

# N = 21
# 2N - 1 = 41
# 41 = 41
# 2k + 3 = 41  ==>  19
# N = 21 + 19 + 1 = 41

# N = 41
# 2N - 1 = 81 = 3^3
# 2k + 3 = 3 ==> k = 0
# N = 41 + 0 + 1 = 42

# N = 42
# 2N - 1 = 83
# 2k + 3 = 83  ==>  k = 40
# N = 42 + 40 + 1 = 83

# N = 83
# 2N - 1 = 165 = 3 * 5 * 11
# 2k + 3 = 3 or 5 or 11  ==>  k = 0
# N = 83 + 0 + 1 = 84

# N = 84
# 2N - 1 = 167
# 2k + 3 = 167 ==> 82
# N = 84 + 82 + 1 = 167

# N = 167
# 2N - 1 = 333 = 3^2 * 37
# 2k + 3 = 3 or 37  ==> k = 0
# N = 167 + 0 + 1 = 168


# g(n) = 3n となる n を生成する
def next_n(n, lim_n):
    while True:
        upper = 2 * n - 1
        p = 3
        while upper % p != 0:
            p += 2
            if p > int(upper**0.5):
                p = upper
        n = n + (p - 3) // 2 + 1
        if n < lim_n:
            yield n
        else:
            break


def main():
    N = 10**15
    n = 9

    for k in next_n(n, N):
        pass
    return 3 * k + (N - k)


if __name__ == '__main__':
    print(main())
