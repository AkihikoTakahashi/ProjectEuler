# coding: utf-8
import copy


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def check3x3(vdata, row, col, val):
    '''row行col列を含む 3x3 のマスにvalを入れられるかチェックする.'''
    r = row // 3 * 3  # row を越えない最大の3の倍数
    c = col // 3 * 3

    used = []
    for x in range(3):
        for y in range(3):
            used.append(vdata[r + y][c + x])
    return val not in used


def solve_sudoku(vdata, idx=0):
    if idx >= 9 * 9:
        return vdata

    row = idx // 9
    col = idx % 9

    # row行col列が 0 でないなら次に進む
    if vdata[row][col] != 0:
        return solve_sudoku(vdata, idx + 1)

    used = [vdata[r][col] for r in range(9)]
    used += vdata[row]
    used = list(set(used))

    for n in range(1, 10):
        if n in used:
            continue
        if not check3x3(vdata, row, col, n):
            continue
        new_data = copy.deepcopy(vdata)
        new_data[row][col] = n

        ret = solve_sudoku(new_data, idx + 1)

        if ret is not None:
            return ret
    return None


def main():
    url = 'https://projecteuler.net/project/resources/p096_sudoku.txt'
    download(url)
    ans = 0
    with open(url.split('/')[-1], 'r') as f:
        for _ in range(50):
            next(f)
            matrix = [list(map(int, next(f).rstrip())) for _ in range(9)]
            solve = solve_sudoku(matrix)
            ans += 100 * solve[0][0] + 10 * solve[0][1] + solve[0][2]
    return ans


if __name__ == '__main__':
    print(main())
