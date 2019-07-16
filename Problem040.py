# coding: utf-8


def main():
    nums = ""
    lim = 1000000
    i = 1
    while len(nums) < lim:
        nums += str(i)
        i += 1

    d = 1
    for e in range(7):
        d *= int(nums[10**e - 1])
    return d


if __name__ == "__main__":
    print(main())
