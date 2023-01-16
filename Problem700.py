# coding: utf-8

# 1504170715041707 と 4503599627370517 は互いに素なので,
# 1504170715041707n = 1 mod 4503599627370517 となる n は存在する.
# よって eulercoin の最小値は 1 である.
# また, そのような n は 3451657199285664 である.
# i = 1, 2, 3, ... 3451657199285664 から探すとすべての eulercoin が見つかるが,
# ループ回数が多すぎるため, 処理が終らない.
#
# ただし, 16 番目の eulercoin 15806432(n = 42298633) までは数秒で見つかる.
# 下のリストを既知の eulercoin とする.
# [
#     1504170715041707, (n=1)
#     8912517754604, (n=3)
#     2044785486369, (n=506)
#     1311409677241, (n=2527)
#     578033868113, (n=4548)
#     422691927098, (n=11117)
#     267349986083, (n=17686)
#     112008045068, (n=24255)
#     68674149121, (n=55079)
#     25340253174, (n=85903)
#     7346610401, (n=202630)
#     4046188430, (n=724617)
#     745766459, (n=1246604)
#     428410324, (n=6755007)
#     111054189, (n=12263410)
#     15806432, (n=42298633)
# ]
#
# つぎに eulercoin を小さいものから見つける.
#
# 1 は eulercoin か判定する.
# x = 1504170715041707, M = 4503599627370517 とする.
# xn = 1 mod M となる n を探す
# ユークリッドの互除法を使うと xn + Ma = 1 なる n が求まる.
# xn = 1 => n = 3451657199285664 である.
# これは既存の eulercoin の中で最も大きいので 1 は eulercoin である.
#
# 2 は eulercoin か判定する.
# xn = 2 となる n を求めるには, 先程もとめた n を使えば,
# x(2n) = 2 mod M であり, 2n = 2399714771200811 mod M となる.
# 2399714771200811 < 3451657199285664 なので 2 は eulercoin である.
#
# 3 は eulercoin か判定する.
# x(3n) = 3 mod M であり, 3n = 1347772343115958 mod M となる.
# 1347772343115958 < 2399714771200811 なので 3 は eulercoin である.
#
# 4 は eulercoin か判定する.
# x(4n) = 4 mod M であり, 4n = 295829915031105 mod M となる.
# 295829915031105 < 1347772343115958 なので 4 は eulercoin である.
#
# 5 は eulercoin か判定する.
# x(5n) = 5 mod M であり, 5n = 3747487114316769 mod M となる.
# 3747487114316769 > 295829915031105 なので 5 は eulercoin ではない.
#
# 6 は eulercoin か判定する.
# x(6n) = 6 mod M であり, 6n = 2695544686231916 mod M となる.
# 2695544686231916 > 295829915031105 なので 6 は eulercoin ではない.
#
# この操作を 15806432 - 1 まで続けると eulercoin がすべて求まる.

from itertools import count


def exgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    q, r = a // b, a % b
    (d, u1, v1) = exgcd(b, r)
    u0 = v1
    v0 = u1 - q * v1

    return (d, u0, v0)


def main():
    EULERCOIN = 1504170715041707
    M = 4503599627370517

    min_eulercoins = EULERCOIN
    eulercoins = [EULERCOIN]

    for n in count(1):
        x = EULERCOIN * n % M
        if x < min_eulercoins:
            min_eulercoins = x
            eulercoins.append(x)
            if x == 15806432:
                break

    EULERCOIN_INV = (exgcd(EULERCOIN, M)[1] + M) % M
    current_inv = EULERCOIN_INV
    known_minimal_eulercoin = min(eulercoins)

    for i in range(1, known_minimal_eulercoin):
        if EULERCOIN_INV * i % M <= current_inv:
            eulercoins.append(i)
            current_inv = EULERCOIN_INV * i % M

    return sum(eulercoins)


if __name__ == '__main__':
    print(main())
