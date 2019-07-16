# coding: utf-8


def next_chain(n):
    from math import factorial

    s = 0
    while n > 0:
        s += factorial(n % 10)
        n //= 10
    return s


def len_chain(n, chain=[], checked=[]):
    if n in checked:
        return len(chain)
    else:
        return len_chain(chains[n], chain + [n], checked + [n])


# 取り得る値の最大値は next_chain(999999) = 9! * 6 = 2177280 より,
# これらの factorial chain を計算しておく.
lim = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 6
chains = {i: next_chain(i) for i in range(lim + 1)}


def main():

    chain60 = 0
    max_i = 1000000
    for i in range(max_i + 1):
        if len_chain(i) == 60:
            chain60 += 1
    return chain60


if __name__ == "__main__":
    print(main())
