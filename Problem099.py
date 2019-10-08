# coding: utf-8

# そのまま計算すると遅いので, 両辺に対数を取って比較する.

from math import log


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    url = 'https://projecteuler.net/project/resources/p099_base_exp.txt'
    download(url)

    max_product = 0
    max_i = 0
    with open(url.split("/")[-1], "r") as f:
        for i, line in enumerate(f):
            b, e = map(int, line.split(','))
            log_n = e * log(b)
            if log_n > max_product:
                max_product = log_n
                max_i = i + 1
    return max_i


if __name__ == '__main__':
    print(main())
