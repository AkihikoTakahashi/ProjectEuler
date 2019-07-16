# coding: utf-8


def cnt_loop(n, m, modulos=[]):
    r = n % m
    if r == 0:
        return 0  # 割り切れるならループしない
    elif r in modulos:
        return len(modulos) - modulos.index(r)
    else:
        return cnt_loop(10 * r, m, modulos + [r])


def main():
    max_d = 1000

    loops = [cnt_loop(1, d) for d in range(1, max_d)]
    return loops.index(max(loops))


if __name__ == "__main__":
    print(main())
