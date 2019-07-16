# coding: utf-8

# レピュニット数 R(k) は下の式で一般項が求まる.
# R(k) = (10^k - 1) / 9
#
# R(k+1) と R(k) との関係は下の式で書ける.
# R(k+1) = 10 * R(k) + 1
#
# また, 両辺に mod n をとると,
# R(k+1) mod n = 10 * R(k) + 1 mod n
#
# A(n) <= n である.
# R(k) = R(l) mod n となる k, l < n が存在するとすれば,
# R(k) mod n から R(l) mod n の値を循環するため A(n) は解を持たなくなる.
# また R(n) mod n は n 通りしかないため, A(n) <= n が言える.


def A(n):
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if _gcd(n, 10) != 1:
        return 0

    x = 1
    k = 1

    while x != 0:
        x = (10 * x + 1) % n
        k += 1
    return k


def main():
    lim = 1000000
    n = lim + 1

    while A(n) < lim:
        n += 2

    return n


if __name__ == "__main__":
    print(main())
