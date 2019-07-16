# coding: utf-8

# 三角形の辺の直線の式を求め, y切片の正負を判定する.
# 原点を含むには X座標, Y座標の正負が異なる必要がある.
# X座標の正負が異なる 2点の直線の式を求め, y切片の正負が
# 異なれば原点を含む.


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def intercept(X, Y):

    # f(X) = (y1-y0)/(x1-x0) * X + b
    # y0 = (y1-y0)/(x1-x0) * x0 + b
    x0, x1 = X[0], Y[0]
    y0, y1 = X[1], Y[1]

    grad = (y1 - y0) / (x1 - x0)
    b = y0 - grad * x0

    return b


def main():
    url = "https://projecteuler.net/project/resources/p102_triangles.txt"
    download(url)

    with open("p102_triangles.txt", "r") as f:
        cnt = 0
        for line in f:
            data = [int(n) for n in line.rstrip().split(",")]
            A = [data[0], data[1]]
            B = [data[2], data[3]]
            C = [data[4], data[5]]

            # X座標がすべて同じ符号なら原点を含まない
            if all(x[0] < 0 for x in [A, B, C]) or all(x[0] > 0
                                                       for x in [A, B, C]):
                continue

            # X座標が A < B < C となるように並べる
            sorted_x = sorted([A, B, C], key=lambda x: x[0])

            A = sorted_x[0]
            B = sorted_x[1]
            C = sorted_x[2]

            if B[0] < 0:
                cnt += int(intercept(A, C) * intercept(B, C) < 0)
            else:
                cnt += int(intercept(A, B) * intercept(A, C) < 0)

    return cnt


if __name__ == "__main__":
    print(main())
