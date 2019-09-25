# coding: utf-8


def cnt_rectangular(n, m):
    return (n * (n + 1) // 2) * (m * (m + 1) // 2)


def main():
    n = 2
    N = 2000000

    diff_min = N
    while cnt_rectangular(n, 1) < N:
        for j in range(1, n):
            rect = cnt_rectangular(n, j)
            diff = abs(rect - N)
            if diff < diff_min:
                diff_min = diff
                surface = n * j
            if rect > N:
                break
        n += 1
    return surface


if __name__ == '__main__':
    print(main())
