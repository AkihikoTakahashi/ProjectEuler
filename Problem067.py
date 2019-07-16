# coding: utf-8

# Problem18 と全く同じやりかたで解ける.


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def max_path(L1, L2):
    better_choice = []
    for i in range(len(L1)):
        better_choice.append(L1[i] + max(L2[i], L2[i + 1]))
    return better_choice


def main():
    url = "https://projecteuler.net/project/resources/p067_triangle.txt"
    download(url)

    with open("p067_triangle.txt", "r") as f:
        L = [[int(n) for n in l.split(" ")] for l in f]

    L.reverse()
    choice = L[0]

    for i in range(len(L) - 1):
        choice = max_path(L[i + 1], choice)

    return choice[0]


if __name__ == "__main__":
    print(main())
