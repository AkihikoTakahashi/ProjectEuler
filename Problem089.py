# coding: utf-8

# ローマ数字を簡略して書く方法は
#
# DCCCC (900) -> CM
# LXXXX (90) -> XC
# VIIII (9) -> IX
# CCCC (400) -> CD
# XXXX (40) -> XL
# IIII (4) -> IV
#
# いずれのパターンも 2 文字で置き換えられる.

import re


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    url = "https://projecteuler.net/project/resources/p089_roman.txt"
    download(url)

    saved_length = 0
    with open(url.split('/')[-1], 'r') as f:
        for line in f:
            s = line.rstrip()
            after_s = re.sub('(DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII)', '**', s)
            saved_length += (len(s) - len(after_s))
    return saved_length


if __name__ == '__main__':
    print(main())
