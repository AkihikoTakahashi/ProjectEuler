# coding: utf-8


def main():

    # m**2 == 1 mod n なる m (1 <= m <= n-1) を返す
    # あらかじめ最小の素因数を格納した smallest_factors を
    # 作っておく
    def self_inverse(n):
        if smallest_factors[n] == n:
            return (1, n - 1)

        else:
            new_sol = []
            p = smallest_factors[n]
            sols = solutions[n // p]
            for i in range(0, n, n // p):
                for j in sols:
                    k = i + j
                    if k * k % n == 1:
                        new_sol.append(k)
            return new_sol

    LIM = 20000000
    end = int(LIM**0.5)
    solutions = [(), (), (1, )]  # n = 0, 1 のとき解なし

    # 各整数 n の最小の素因数を求める
    # smallest_factors[n] == n なら n は素数となる
    smallest_factors = [0] * (LIM + 1)
    for i in range(2, len(smallest_factors)):
        if smallest_factors[i] == 0:
            smallest_factors[i] = i
            if i <= end:
                for j in range(i**2, len(smallest_factors), i):
                    if smallest_factors[j] == 0:
                        smallest_factors[j] = i

    ans = 0
    for i in range(3, LIM + 1):
        sols = self_inverse(i)
        if i <= LIM // 2:
            solutions.append(sols)
        ans += sols[-2]
    return ans


if __name__ == '__main__':
    print(main())
