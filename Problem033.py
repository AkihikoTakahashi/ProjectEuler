# coding: utf-8


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    prod_a = 1
    prod_b = 1
    for a in range(11, 99):
        for b in range(a + 1, 100):

            a_10, a_1 = a // 10, a % 10
            b_10, b_1 = b // 10, b % 10

            # 1桁目が 0 なら trivial
            if a_1 == 0 or b_1 == 0:
                continue

            # 文字として約分できなければ次へ
            if not a_1 in [b_10, b_1] or a_10 in [b_10, b_1]:
                continue

            if a_10 == b_10:
                aft_a = a_1
                aft_b = b_1
            elif a_10 == b_1:
                aft_a = a_1
                aft_b = b_10
            elif a_1 == b_10:
                aft_a = a_10
                aft_b = b_1
            elif a_1 == b_1:
                aft_a = a_10
                aft_b = b_10

            if a / b == aft_a / aft_b:
                prod_a *= aft_a
                prod_b *= aft_b

    return prod_b // gcd(prod_a, prod_b)


if __name__ == "__main__":
    print(main())
