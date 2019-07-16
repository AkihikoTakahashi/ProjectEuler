# coding: utf-8

# dp を N行N列の配列とする.
# dp[j][i-1] までの最小値とすると, dp[j][i] は
# dp[0][i-1] + dp[0][i] + dp[1][i] + dp[2][i] + ... + dp[j][i],
# dp[1][i-1] + dp[1][i] + dp[2][i] + ... + dp[j][i],
# ...
# dp[j][i-1] + dp[j][i],
# ...
# dp[N][i-1] + dp[N][i] + dp[N-1][i] + ... + dp[j][i]
# の最小値となる.


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    url = "https://projecteuler.net/project/resources/p082_matrix.txt"
    download(url)

    with open(url.split("/")[-1], "r") as f:
        data = [[int(i) for i in line.rstrip().split(",")]
                for line in f.readlines()]

    size = len(data)
    dp = [[0] * size for _ in range(size)]
    for j in range(size):
        dp[j][0] = data[j][0]

    for i in range(1, size):

        left_i = [x[i - 1] for x in dp]
        col_i = [x[i] for x in data]

        for j in range(size):

            # dp[j][i] を計算する.
            min_path = left_i[j] + col_i[j]

            sum_col = col_i[j]
            for k in range(j - 1, -1, -1):
                sum_col += col_i[k]
                min_path = min(min_path, sum_col + left_i[k])

            sum_col = col_i[j]
            for k in range(j + 1, size):
                sum_col += col_i[k]
                min_path = min(min_path, sum_col + left_i[k])

            dp[j][i] = min_path
    return min(x[-1] for x in dp)


if __name__ == "__main__":
    print(main())
