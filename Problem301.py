# coding: utf-8

# Nim は (a, b, c) のとき, a xor b xor c = 0 のとき後手必勝である.
# よって, a xor 2a xor 3a = 0 となる a (0 <= a <= 2^30) が
# 何個あるか数えればよい.
#
# a xor a = 0 より a xor 2a = 3a となればよい.
# a を 2進数表記したとき, 2a は a を 1 桁左にずらし末尾に 0 を付け
# 足したものなので, a の 2進数表記したとき 1 が連続しなければ,
# a xor 2a = 3a となる.
#
# 2進数 n 桁で末尾が 0 のものを a_n, 1 のものを b_n とし,
# c_n = a_n + b_n とおく.
# n+1 桁目が 0 になる個数は n 桁目が 0 の個数 + n 桁目が 1 の個数なので
# a_n+1 = a_n + b_n が成り立つ.
# n+1 桁目が 1 になる個数は n 桁目が 0 の個数なので
# b_n+1 = a_n が成り立つ.
# よって
# c_n+1 = a_n+1 + b_n+1 = (a_n + b_n) + a_n
#       = c_n + (a_n-1 + b_n-1) = c_n + c_n-1
#
# ゆえに c_n はフィボナッチ数列となる.
#
# よって a <= 2^30 - 1 のとき, 2進数表記が 1 が続かないような a は
# f(1) + f(2) + ... + f(30) であり, a= 2^30 も 2進数表記で 1 が
# 続かないので f(1) + f(2) + ... + f(30) + 1 が解となる.
# (ただし f(n) はフィボナッチ数列の第 n 項)
#
# Σf(k) = f(k+2) - 1 が成り立つので,
# f(1) + ... + f(30) + 1 = (f(32) - 1) + 1 = f(32) より
# f(32) が解となる.


def main():
    d = 30
    a, b = 0, 1
    for i in range(d + 2):
        a, b = a + b, a
    return a


if __name__ == '__main__':
    print(main())
