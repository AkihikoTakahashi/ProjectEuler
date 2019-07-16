# coding: utf-8

# 1p 硬貨と 2p 硬貨を使って 5p の両替を考える.
#
# 1. 1p 硬貨のみを使う方法は明らかにすべて1通りしかない.
# |------+---+---+---+---+---+---|
# | P    | 0 | 1 | 2 | 3 | 4 | 5 |
# |------+---+---+---+---+---+---|
# | 通り | 1 | 1 | 1 | 1 | 1 | 1 |
# |------+---+---+---+---+---+---|
#
# 2. 2p 硬貨を使って 5p の両替を考える.
# 2.1. 2p 硬貨を使って 0p, 1p の両替する方法は両替元の値段
#         を超てるため 0 通り,
# |------+---+---+---+---+---+---|
# | P    | 0 | 1 | 2 | 3 | 4 | 5 |
# |------+---+---+---+---+---+---|
# | 通り | 1 | 1 | 1 | 1 | 1 | 1 |
# |------+---+---+---+---+---+---|
#
# 2.2. 2p 硬貨を使って 2p の両替する方法は 1 通り.
#         (なぜなら 2p-2p=0pを両替する方法は 1 通りだから)
#         2p の両替方法に 1 加える.
# |------+---+---+---+---+---+---|
# | P    | 0 | 1 | 2 | 3 | 4 | 5 |
# |------+---+---+---+---+---+---|
# | 通り | 1 | 1 | 2 | 1 | 1 | 1 |
# |------+---+---+---+---+---+---|
#
# 2.3. 2p 硬貨を使って 3p の両替する方法は 1 通り.
#         (なぜなら 3p-2p=1pを両替する方法は 1 通りだから)
#         3p の両替方法に 1 加える.
# |------+---+---+---+---+---+---|
# | P    | 0 | 1 | 2 | 3 | 4 | 5 |
# |------+---+---+---+---+---+---|
# | 通り | 1 | 1 | 2 | 2 | 1 | 1 |
# |------+---+---+---+---+---+---|
#
# 2.4. 2p 硬貨を使って 4p の両替する方法は 2 通り.
#         (なぜなら 4p-2p=2pを両替する方法は 2 通りだから)
#         4p の両替方法に 2 加える.
# |------+---+---+---+---+---+---|
# | P    | 0 | 1 | 2 | 3 | 4 | 5 |
# |------+---+---+---+---+---+---|
# | 通り | 1 | 1 | 2 | 2 | 3 | 1 |
# |------+---+---+---+---+---+---|
#
# 2.5. 2p 硬貨を使って 5p の両替する方法は 2 通り.
#         (なぜなら 5p-2p=3pを両替する方法は 2 通りだから)
#         5p の両替方法に 2 加える.
# |------+---+---+---+---+---+---|
# | P    | 0 | 1 | 2 | 3 | 4 | 5 |
# |------+---+---+---+---+---+---|
# | 通り | 1 | 1 | 2 | 2 | 3 | 3 |
# |------+---+---+---+---+---+---|
#
# まとめると, C硬貨を使ってNpにするには (N-C)p 通り加算すればよい.


def main():
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    target = 200

    way = [0] * (target + 1)
    way[0] = 1
    for coin in coins:
        for i in range(coin, len(way)):
            way[i] += way[i - coin]
    return way[-1]


if __name__ == "__main__":
    print(main())