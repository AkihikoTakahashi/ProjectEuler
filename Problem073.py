# coding: utf-8


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def main():
    lim = 12000
    cnt = 0
    # d = 3, 4 のときは解なし
    for d in range(5, lim + 1):
        # 1/3 < a/d < 1/2 => d/3 < a < d/2
        for a in range(d // 3 + 1, d // 2 + 1):
            if gcd(a, d) == 1:
                cnt += 1
    return cnt


if __name__ == '__main__':
    print(main())
