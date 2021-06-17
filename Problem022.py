# coding: utf-8


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def point(n, name):
    return n * sum(ord(s) - ord("A") + 1 for s in name)


def main():
    url = "https://projecteuler.net/project/resources/p022_names.txt"
    download(url)

    with open("p022_names.txt", "r") as f:
        for line in f:
            names = [x[1:-1] for x in line.split(",")]

    names.sort()
    return sum([point(i + 1, name) for i, name in enumerate(names)])


if __name__ == '__main__':
    print(main())
