# coding: utf-8

# e^(k/n) - 1 >= π となる最小の k は int(n * log(π+1))+1

import math


def f_n(n):
    E = math.e

    def _f(a):
        return E**(a / n) - 1

    return _f


def main():
    n = 10000
    PI = math.pi

    f = f_n(n)
    max_k = int(n * math.log(PI + 1)) + 1
    f_lists = [f(i) for i in range(max_k)]
    f_dict = dict()

    for a in range(max_k):
        for b in range(a + 1, max_k):
            if f_lists[a] + f_lists[b] > PI:
                break
            f_dict[(a, b)] = f_lists[a] + f_lists[b]

    error_min = 1e9
    for k1, v1 in f_dict.items():
        for k2, v2 in f_dict.items():
            a, b = k1
            c, d = k2

            if b > c:
                continue

            error = v1 + v2 - PI

            if abs(error) < error_min:
                error_min = abs(error)
                a_min, b_min, c_min, d_min = a, b, c, d
    print(a_min, b_min, c_min, d_min)
