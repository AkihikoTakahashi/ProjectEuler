# coding: utf-8


def cfrac(d):
    p, q = 0, 1
    x = int(d**0.5)

    check = []
    while True:
        a = (x + p) // q
        p = a * q - p
        q = (d - p * p) // q

        if [p, q] in check:
            return (len(check) - check.index([p, q])) % 2 == 1
        check.append([p, q])


def main():
    n = 10000
    return sum(cfrac(i) for i in range(2, n + 1) if int(i**0.5)**2 != i)
