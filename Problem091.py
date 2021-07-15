# coding: utf-8

from math import gcd


def main():
    lim_x = 50
    lim_y = 50
    cnt = lim_x * lim_y * 3

    for x1 in range(1, lim_x + 1):
        for y1 in range(1, lim_y + 1):
            g = gcd(x1, y1)
            dx = y1 // g
            dy = x1 // g
            cnt += min((lim_x - x1) // dx, y1 // dy) * 2

    return cnt


if __name__ == '__main__':
    print(main())
