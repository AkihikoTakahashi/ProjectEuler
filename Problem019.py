# coding: utf-8


def is_leap(n):
    return n % 4 == 0 and n % 100 != 0 or n % 400 == 0


def main():
    start_y = 1900
    end_y = 2000
    weekday = 1  # 月曜
    day = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]  # day[0] は 12月
    cnt = 0

    for year in range(start_y, end_y + 1):
        day[2] = 29 if is_leap(year) else 28

        for month in range(1, 12 + 1):

            weekday = (weekday + day[month % 12]) % 7

            if year < 1901:
                continue

            if weekday == 0:
                cnt += 1
    return cnt


if __name__ == "__main__":
    print(main())
