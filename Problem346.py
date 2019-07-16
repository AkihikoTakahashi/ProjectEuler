# coding: utf-8

# 7は2進数, 6進数でレピュニット数となる.
# 7(10) = 111(2), 7(10) = 11(6)
#
# 一般に任意の自然数 N に対して N(10) = 11(N-1) である.
# よって
# 111(2), 111(3), 111(4), ...
# 1111(2), 1111(3), 1111(4), ...
# 11111(2), 11111(3), 11111(4), ...
# ...
# を求め、重複削除後に合計すればよい.


def to_int(s, base):
    n = 0
    while s != "":
        n = base * n + int(s[0])
        s = s[1:]
    return n


def main():

    base = 2
    s_repunits = [1]
    lim = 10**12
    while base <= lim**0.5:
        b = "111"
        while to_int(b, base) < lim:
            s_repunits.append(to_int(b, base))
            b += "1"
        base += 1
    return sum(set(s_repunits))


if __name__ == "__main__":
    print(main())
