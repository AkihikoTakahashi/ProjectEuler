# coding: utf-8

# 最近点対問題のコードがそのまま使える
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7429599#1

from itertools import islice
from math import sqrt
import operator


def gen_s(s, M):
    s0 = s
    s1 = pow(s, 2, M)

    while True:
        yield s0, s1
        s0 = pow(s1, 2, M)
        s1 = pow(s0, 2, M)


def closest_pair(point_list):
    n = len(point_list)
    if n <= 1:
        return float('inf')

    mid = n // 2
    x = point_list[mid][0]
    d = min(
        closest_pair(point_list[:mid]),
        closest_pair(point_list[mid:]),
    )

    point_list.sort(key=operator.itemgetter(1))

    py_list = []
    for p in point_list:
        if abs(p[0] - x) >= d:
            continue
        for py in reversed(py_list):
            dx = abs(py[0] - p[0])
            dy = abs(py[1] - p[1])

            if dy >= d:
                break
            d = min(d, sqrt(dx**2 + dy**2))

        py_list.append(p)

    return d


def main():
    M = 50515093
    s0 = 290797
    n = 2000000
    points = [p for p in islice(gen_s(s0, M), n)]

    points.sort(key=operator.itemgetter(0))

    return round(closest_pair(points), 9)


if __name__ == '__main__':
    print(main())
