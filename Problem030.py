# coding: utf-8

# 99999 < 9**5 + 9**5 + ... + 9**5 = 295245
# 999999 > 9**5 + 9**5 + ... + 9**5 = 354294
# より 6桁の各桁の5乗の和は 354294 となり上限となる.


def main():
    lim = 6 * 9**5

    s = 0
    for n in range(2, lim + 1):
        if n == sum(int(x)**5 for x in str(n)):
            s += n
    return s


if __name__ == "__main__":
    print(main())
