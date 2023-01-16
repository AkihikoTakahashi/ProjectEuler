# coding: utf-8


def download(url):
    import urllib.request
    import os

    save_name = url.split('/')[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def main():
    def d(x, y):
        if x < 0 or y < 0 or x >= w or y >= h:
            return float('inf')
        else:
            return distance[y][x]

    url = "https://projecteuler.net/project/resources/p083_matrix.txt"
    download(url)

    with open('p083_matrix.txt', 'r') as f:
        matrix = [[int(n) for n in l.split(',')] for l in f]

    h = len(matrix)
    w = len(matrix[0])

    distance = [[float('inf')] * w for _ in range(h)]

    distance[0][0] = matrix[0][0]

    # ベルマンフォード法
    changed = True
    while changed:
        changed = False
        for y in range(h):
            for x in range(w):
                tmp = matrix[y][x] + min(
                    d(x - 1, y), d(x + 1, y), d(x, y - 1), d(x, y + 1)
                )
                if tmp < distance[y][x]:
                    distance[y][x] = tmp
                    changed = True

    return distance[-1][-1]


if __name__ == '__main__':
    print(main())
