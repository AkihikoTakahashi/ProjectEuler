# coding: utf-8


def main():

    L = 250250
    M = 250
    MOD = 10**16

    # dp[i] には「合計が 250 で割ったあまりが i になる部分集合」の個数をいれる
    dp = [0] * M

    dp[0] = 1
    for i in range(1, L + 1):
        v = pow(i, i, M)
        dp = [(d + dp[(j - v) % M]) % MOD for j, d in enumerate(dp)]
    return dp[0] - 1


if __name__ == '__main__':
    print(main())
