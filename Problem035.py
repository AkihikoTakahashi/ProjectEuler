# coding: utf-8

# N が回転も含めてすべての数が素数となるには N = 2, 5 を除き,
# N のすべての桁に偶数と 5 がこないことが必要条件である.


def eratosthenes(n):

    primes = [False if i % 2 == 0 else True for i in range(n + 1)]
    primes[1], primes[2] = False, True

    for i in range(int(n**0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False

    return primes


def main():
    max_n = 1000000
    primes = eratosthenes(max_n)

    cnt = 2  # 2, 5は明らかに条件を満たす
    for n in range(3, max_n + 1, 2):
        str_n = str(n)

        if any(int(i) % 2 == 0 or int(i) == 5 for i in str_n):
            continue

        rotate_n = [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]
        if all(primes[n] for n in rotate_n):
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(main())
