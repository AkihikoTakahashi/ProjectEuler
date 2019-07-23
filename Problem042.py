# coding: utf-8

# n = x(x+1)/2 より x = (√(8n+1)-1)/2
# よって (√(8n+1)-1)/2 が自然数なら n は三角数.


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def is_triangle(n):
    tmp_n = ((8 * n + 1)**0.5 - 1) / 2.0
    return tmp_n == int(tmp_n)


def word2num(word):
    return sum(ord(x) - ord('A') + 1 for x in word)


def main():
    url = "https://projecteuler.net/project/resources/p042_words.txt"
    download(url)

    with open(url.split("/")[-1], "r") as f:
        for line in f:
            data = [x[1:-1] for x in line.rstrip().split(",")]

    return sum(is_triangle(word2num(x)) for x in data)


if __name__ == "__main__":
    print(main())
