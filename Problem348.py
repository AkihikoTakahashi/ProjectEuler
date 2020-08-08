# coding: utf-8


def find_n(sorted_list, n):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        i = (left + right) // 2
        if sorted_list[i] == n:
            return True
        elif sorted_list[i] < n:
            left = i + 1
        else:
            right = i - 1
    return False


def gen_palindromic(digit=0):
    '''digit桁の回文数を生成する'''

    from itertools import count

    def _gen_palindromic(digit, length=0):

        if digit == length:
            yield 0
        elif digit - 1 == length:
            for i in range(10):
                yield i
        else:
            start_i = 1 if length == 0 else 0
            multi = 10**(digit - length - 1) + 1
            for i in range(start_i, 10):
                for palindromic in _gen_palindromic(digit, length + 2):
                    yield i * multi + 10 * palindromic

    for d in count(digit):
        for p in _gen_palindromic(d):
            yield p


def main():
    WAYS = 4
    COUNT = 5
    squares = []
    cubes = []
    s_max = 1
    c_max = 1
    cnt = 0
    pal_sum = 0

    for pal in gen_palindromic():
        way = 0

        # pal 以下の平方数のリストを生成
        while s_max**2 < pal:
            squares.append(s_max**2)
            s_max += 1

        # pal 以下の立方数のリストを生成
        while c_max**3 < pal:
            cubes.append(c_max**3)
            c_max += 1

        for c in cubes:
            if find_n(squares, pal - c):
                way += 1

        if way == WAYS:
            cnt += 1
            pal_sum += pal

        if cnt == COUNT:
            return pal_sum


if __name__ == '__main__':
    print(main())
