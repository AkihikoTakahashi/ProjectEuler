# coding: utf-8

from itertools import count


def triangle(i):
    return i * (i + 1) // 2


def square(i):
    return i**2


def pentagonal(i):
    return i * (3 * i - 1) // 2


def hexagonal(i):
    return i * (2 * i - 1)


def heptagonal(i):
    return i * (5 * i - 3) // 2


def octagonal(i):
    return i * (3 * i - 2)


def is_circlic(n1, n2):
    return str(n1)[-2:] == str(n2)[:2]


def find(figure_nums, nums=[], find_list={0, 1, 2, 3, 4, 5}):
    if len(nums) == 6 and is_circlic(nums[-1], nums[0]):
        return nums + [0]

    for i in find_list:  # 0 <= i <= 5
        for new_n in figure_nums[i]:
            if len(nums) == 0 or is_circlic(nums[-1], new_n):
                f = find(figure_nums, nums + [new_n], find_list - {i})
                if len(f) == 7:
                    return f
    return nums


def main():
    figure_nums = []
    for f in [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]:
        figs = []
        for i in count(1):
            n = f(i)
            if n < 1000:
                continue
            if n >= 10000:
                break
            figs.append(n)
        figure_nums.append(figs)
    return sum(find(figure_nums))


if __name__ == '__main__':
    print(main())
