# coding: utf-8

num_dict = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def num2word(n, s=""):
    if n in num_dict:
        return s + num_dict[n]

    if 21 <= n < 100:
        str_n = num_dict[int(n / 10) * 10]
        return num2word(n % 10, s + str_n)
    if 100 <= n < 1000:
        str_n = num_dict[int(n / 100)] + "hundred"
        if n % 100 != 0:
            str_n += "and"
        return num2word(n % 100, s + str_n)
    if 1000 == n:
        str_n = num_dict[int(n / 1000)] + "thousand"
        if n % 1000 != 0:
            str_n += "and"
        return num2word(n % 1000, s + str_n)


def main():
    lim = 1000
    cnt = 0
    for i in range(lim + 1):
        cnt += len(num2word(i))
    return cnt


if __name__ == "__main__":
    print(main())
