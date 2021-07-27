# coding: utf-8

from itertools import product, cycle
from collections import Counter


def download(url):
    import urllib.request
    import os

    save_name = url.split('/')[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    url = 'https://projecteuler.net/project/resources/p059_cipher.txt'
    download(url)

    key_len = 3
    with open(url.split('/')[-1], "r") as f:
        ciphers = []
        for line in f:
            ciphers += [int(i) for i in line.split(',')]

    for keys in product(range(ord('a'), ord('z') + 1), repeat=3):
        plain = ''
        s = 0

        for i, cipher in zip(cycle(range(key_len)), ciphers):
            plain += chr(cipher ^ keys[i])
            s += cipher ^ keys[i]

        # the, The を含んでいれば正しいとみなす
        if ' the ' in plain or ' The ' in plain:
            return s


if __name__ == '__main__':
    print(main())
