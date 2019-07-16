# coding: utf-8

from itertools import count, combinations


def is_prime(n):
    return n % 2 != 0 and all(
        [n % i != 0 for i in range(3,
                                   int(n**0.5) + 1, 2)])


def replace_num(str_num, l_digit, str_n):
    """str_num の l_digit 桁目を n に置き換える"""
    for d in l_digit:
        str_num = str_num[:d] + str_n + str_num[d + 1:]
    return str_num


def main():

    # Tips: 1の位を置換しても素数は5つ以上できない.
    checked = []  # すでに確認済みのリスト
    find_goal = 8
    nums = "1234567890"
    for n in count(11, 2):

        if n % 5 == 0 or n in checked:
            continue

        str_n = str(n)

        # replace_cnt は 置換する桁の個数
        for replace_cnt in range(1, len(str_n)):

            # 何桁目を置換するかの組合せ
            # 1の位は置換候補に入れないので range(len(str_n)-1)
            for digits in combinations((j for j in range(len(str_n) - 1)),
                                       replace_cnt):
                answers = []

                # どの数字に置換するかの組合せ
                for change in nums:

                    # 先頭桁を0に置換しない
                    if digits[0] == 0 and change == "0":
                        continue

                    replaced_n = int(replace_num(str_n, digits, change))
                    checked.append(replaced_n)

                    if is_prime(replaced_n):
                        answers.append(replaced_n)
                    if len(answers) == find_goal:
                        return min(answers)


if __name__ == "__main__":
    print(main())
