# coding: utf-8


def is_square(n):
    return int(n**0.5) ** 2 == n


def main():
    solved = False

    i = 4
    while not solved:
        a = i**2

        for j in range(3, i):
            if solved:
                break

            c = j**2
            f = a - c
            if not is_square(f):
                continue

            k_init = 2 if j % 2 == 0 else 1

            for k in range(k_init, j, 2):
                d = k**2
                e = a - d
                b = c - e

                if b <= 0 or not is_square(e) or not is_square(b):
                    continue

                x = (a + b) // 2
                y = (e + f) // 2
                z = (c - d) // 2
                result = x + y + z
                solved = True

                break
        i += 1

    return result


if __name__ == '__main__':
    print(main())
