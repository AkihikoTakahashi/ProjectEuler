# coding: utf-8

# Tips: X^2 = 1_2_3_4_5_6_7_8_9_0 ならば
#       1010101010 < X < 1389026623 であり,
#       X^2 mod 10 = 0 ==> X mod 10 = 0 となる.


def check(n):
    for i in range(10):
        if not n % 10 == 9 - i:
            return False
        n //= 100

    return True


def main():
    min_x = int(1020304050607080900**0.5)
    max_x = int(1929394959697989990**0.5)

    for x in range(min_x // 10 * 10, max_x, 10):
        if check(x**2 // 100):
            return x


if __name__ == "__main__":
    print(main())
