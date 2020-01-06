# coding: utf-8


def is_permute(n1, n2):
    def gen_digit(n):
        while n > 0:
            yield n % 10
            n //= 10

    return sorted(gen_digit(n1)) == sorted(gen_digit(n2))


def list_totients(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:  # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result


def main():
    N = 10**7
    totients = list_totients(N)
    min_rat = 87109 / 79180  # 問題文より高々この値
    for i, tot in enumerate(totients[2:], 2):
        if is_permute(i, tot):
            rat = i / tot
            if rat < min_rat:
                min_rat = rat
                min_i = i
    return min_i


if __name__ == '__main__':
    print(main())
