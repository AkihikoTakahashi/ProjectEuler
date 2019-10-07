# coding: utf-8

# 最後に k を足して n にする方法は
# dp[n] = dp[n] + dp[n-k]
# で書ける.


def main():
    N = 100
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N):
        for j in range(i, N + 1):
            dp[j] += dp[j - i]
    return dp[-1]


if __name__ == '__main__':
    print(main())
