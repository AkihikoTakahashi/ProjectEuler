# coding: utf-8

# 一応動くが 40min 要する.
#
# n を平方数とする.
# n を分割した合計を s とすると,
# s = Σ(10^e_i * a_i) と書ける. (e_i は a_i の桁数 - 1)
# 10^e = 1 mod 9 より s mod 9 は n の分割方法に依らず一定.
#
# よって, n mod 9 = s mod 9
# √n = s であるためには, √n = n mod 9 より
# n = 0, 1 mod 9

# from itertools import chain, combinations
# from math import log10

# def gen_digit(n):
#     nums = []

#     while n > 0:
#         nums.append(n % 10)
#         n //= 10
#     return reversed(nums)

# def subsets(iterable):
#     '''nums の部分集合を返す.'''

#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# def partitions(iterable):
#     seq = list(iterable)
#     n = len(seq)
#     for i in subsets(range(1, n)):
#         yield [seq[i:j] for i, j in zip((0, ) + i, i + (n, ))]

# def list2num(nums):
#     s = 0
#     for n in nums:
#         s = s * 10 + n
#     return s

# def is_sNumber(n):
#     '''n が sNumber か調べる. ただし n は平方数であること.'''
#     d = int(log10(n)) + 1
#     for ns in partitions(gen_digit(n)):
#         # i 桁の数 n に対して分割された数は i/2 桁を含む必要がある.
#         if not any(len(k) >= d // 2 for k in ns):
#             continue
#         split_nums = [list2num(i) for i in ns]
#         sum_split = sum(split_nums)
#         if n == sum_split**2:
#             # print(n, split_nums)
#             return True
#     return False


# スレッドで見つけた, より効率のよいコード
def sum_partition(a, b):
    '''bを分割して合計したものを a と等しくできるか判定する'''
    if a == b:
        return True
    d = 10
    while d < b:
        p, q = b // d, b % d
        if 0 < a - q <= p and sum_partition(a - q, p):
            return True
        d *= 10
    return False


def main():
    N = 10**12
    return sum(i**2
               for i in filter(lambda x: x % 9 <= 1, range(4,
                                                           int(N**0.5) + 1))
               if sum_partition(i, i**2))


if __name__ == '__main__':
    print(main())
