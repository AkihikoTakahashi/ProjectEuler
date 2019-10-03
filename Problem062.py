# coding: utf-8


def sort_n(n):
    def _gen_digit(n):
        while n > 0:
            yield n % 10
            n //= 10

    return tuple(sorted(i for i in _gen_digit(n)))


def gen_cube():
    n = 1
    while True:
        yield n**3
        n += 1


def main():

    cubes = {}
    cube_nums = {}
    CNT = 5
    for n in gen_cube():
        nums = sort_n(n)
        if nums in cubes:
            cubes[nums] += 1
        else:
            cubes[nums] = 1
            cube_nums[nums] = n

        if cubes[nums] == CNT:
            break
    return cube_nums[nums]


if __name__ == '__main__':
    print(main())
