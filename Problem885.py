# coding: utf-8

# 愚直の1桁から3桁の数とその個数を羅列すると
# {1: 3, 2: 3, ..., 9: 3, 11: 3, 12: 6, ..., 22: 3, 23: 6, ..., 689: 6, 777: 1, 789: 6, 888: 1, 889: 3, 899: 3 }
# となり, その合計 1*3 + 2*3 + ... + 9*3 + 11*3 + 12*6 + ... + 22*3 + 23*6 + ... + 888*1 + 889*3 + 899*3 が解となる.
#
# 各桁をソートしたときに 123, 133 になる数が何通りあるか考える.
# 123 は 123, 132, 213, 231, 312, 321 の6つとなる
# 133 は 133, 313, 331 の3つとなる
# つまり, 重複を含む並べ方なので d! / (d_0! * d_1! * d_2! * ...) で求まる.
# (d は桁数, d_i は i の個数)


from collections import Counter
from math import factorial


def permutation(n, d):
    '''d桁でnを表現したときの並べ方'''
    str_n = str(n).zfill(d)
    c = Counter(str_n)
    p = factorial(len(str_n))
    for i in c.values():
        p //= factorial(i)

    return p


# combination_with_replacement(range(10), d)で十分
def gen_ascending_num(d, start=0, increasing_num=0):
    '''d桁以下の同じ数を含む増加数を生成する'''
    if d == 0:
        yield increasing_num

    else:
        for i in range(start, 10):
            new_increasing_num = increasing_num * 10 + i
            yield from gen_ascending_num(d - 1, i, new_increasing_num)


def main():
    s = 0
    d = 18
    M = 1123455689

    # 18桁の増加数は 27C9 = 4686825 で十分にループで処理できる
    for k in gen_ascending_num(d):
        v = permutation(k, d)
        s += k * v
        s %= M
    return s


if __name__ == '__main__':
    print(main())
