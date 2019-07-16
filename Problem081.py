# coding: utf-8

# 動的計画法を使う.
# data[k][l] を k 行 l 列目までの最小値が格納されたとして,
# data[j][i] は data[j-1][i] か data[j][i-1] の小さいほうを加えればよい.


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    url = "https://projecteuler.net/project/resources/p081_matrix.txt"
    download(url)

    with open("p081_matrix.txt", "r") as f:
        data = [[int(i) for i in line.rstrip().split(",")]
                for line in f.readlines()]

    height = len([i[0] for i in data])
    width = len(data[0])

    for j in range(1, width):
        data[0][j] += data[0][j - 1]

    for i in range(1, height):
        data[i][0] += data[0][i - 1]

    for i in range(1, width):
        for j in range(1, height):
            data[j][i] += min(data[j - 1][i], data[j][i - 1])
    return data[-1][-1]


if __name__ == "__main__":
    print(main())
