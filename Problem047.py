# coding: utf-8


def cnt_factor(n):

    i = 2
    factors = set()
    while i < n**0.5 or n == 1:
        if n % i == 0:
            factors.add(i)
            n //= i
            i -= 1
        i += 1
    return len(factors) + 1


def main():
    N = 4
    i = 2 * 3 * 5 * 7
    flag = 0
    while True:
        if cnt_factor(i) == N:
            flag += 1
        else:
            flag = 0
        if flag == N:
            break
        i += 1
    return i - N + 1


if __name__ == "__main__":
    print(main())
