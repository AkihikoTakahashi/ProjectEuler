# coding: utf-8

# 1 の前: 3, 7
# 2 の前: 1, 3, 6, 7
# 3 の前: 7
# 4 の前: テキストになし
# 5 の前: テキストになし
# 6 の前: 1, 3, 7
# 7 の前: なし
# 8 の前: 1, 2, 3, 6, 7
# 9 の前: 1, 2, 3, 6, 7, 8
# 0 の前: 1, 2, 3, 6, 7, 8, 9

# 以上からコードに使われる数字は 0, 1, 2, 3, 6, 7, 8, 9 であり,
# 7 の前に来る数字がないことから, コードの先頭は 7 であることが分る.
# 3 の前に来る数字が 7 しかなく, 3 と 7 を除く他の数字の前に 3 が
# 来ることから, コードは 73 と続く.
# 1 の前に来る数字が 3, 7 しかなく, 3, 7, 1 を除く他の数字の前に 1 が
# 来ることから, コードは 731 と続く.
# 同様にすることで, コードは 73162890 であることが分る.


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    url = 'https://projecteuler.net/project/resources/p079_keylog.txt'
    download(url)

    return 73162890


if __name__ == '__main__':
    print(main())
