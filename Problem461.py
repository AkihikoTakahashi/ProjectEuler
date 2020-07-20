# coding: utf-8

# e^(k/n) - 1 >= π となる最小の k は int(n * log(π+1))+1

import math


def binary_search_closest(numbers, target):
    '''2分探索をする.
値が存在しない場合, 近似値を返す

今回のnumbersのフォーマットは (num, a, b)であり, targetに一致する num を探す'''

    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0]

    minimum_diff = float('inf')

    i_min = 0
    i_max = len(numbers) - 1
    closest = None

    while i_min <= i_max:
        i_middle = i_min + (i_max - i_min) // 2

        if i_middle + 1 < len(numbers):
            diff_right = abs(numbers[i_middle + 1][0] - target)
        if i_middle > 0:
            diff_left = abs(numbers[i_middle - 1][0] - target)

        if diff_left < minimum_diff:
            minimum_diff = diff_left
            closest = numbers[i_middle - 1]
        if diff_right < minimum_diff:
            minimum_diff = diff_right
            closest = numbers[i_middle + 1]

        if numbers[i_middle][0] < target:
            i_min = i_middle + 1
        elif numbers[i_middle][0] > target:
            i_max = i_middle - 1
        else:
            return numbers[i_middle][0]
    return closest


def f_n(n):
    E = math.e

    def _f(a):
        return E**(a / n) - 1

    return _f


def main():
    n = 10000
    # n = 200
    PI = math.pi

    f = f_n(n)
    max_k = int(n * math.log(PI + 1)) + 1
    f_lists = [f(i) for i in range(max_k)]

    f_plus_g = []
    for a in range(1, max_k):
        for b in range(a + 1, max_k):
            if f_lists[a] + f_lists[b] > PI:
                break
            f_plus_g.append((f_lists[a] + f_lists[b], a, b))
    sorted_f_plus_g = sorted(f_plus_g, key=lambda x: x[0])

    error_min = 10
    for k1, a, b in sorted_f_plus_g:
        if k1 > PI / 2:
            break
        k2, c, d = binary_search_closest(sorted_f_plus_g, PI - k1)
        error = abs(k1 + k2 - PI)
        if error < error_min:
            a_min, b_min, c_min, d_min = a, b, c, d
            error_min = error
    return a_min**2 + b_min**2 + c_min**2 + d_min**2


if __name__ == '__main__':
    print(main())
