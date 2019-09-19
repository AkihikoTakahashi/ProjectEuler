# coding: utf-8

# abcd + dcba の各桁が奇数となるためには a と d の偶奇が異なる必要がある.
# また, 問題文より 1 桁目が 0 も除外する.
#
# これでも答えは見つかるが, 20分以上かかる.
# N=10**8 と N=10**9 が同じ結果なのでもっといい方法があるはず.


def rev(num):
    n = 0
    while num > 0:
        n = n * 10 + num % 10
        num //= 10
    return n


def head(num):
    while num > 9:
        num //= 10
    return num


def main():
    N = 10**9
    cnt = 0
    for i in range(N):
        if i % 10 == 0:
            continue
        if i & 1 == head(i) & 1:
            continue

        n = i + rev(i)
        while n > 0:
            if (n % 10) & 1 == 0:
                break
            n //= 10
        else:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(main())
