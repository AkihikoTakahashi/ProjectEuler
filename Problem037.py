# coding: utf-8


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])


def main():
    cnt = 0
    lim = 11
    s = 0

    n = 11
    while cnt < lim:
        if is_prime(n):
            str_n = str(n)
            if all(is_prime(int(str_n[:i]))
                   for i in range(1, len(str_n))) and all(
                       is_prime(int(str_n[i:])) for i in range(1, len(str_n))):
                cnt += 1
                s += n
        n += 2

    return s


if __name__ == "__main__":
    print(main())
