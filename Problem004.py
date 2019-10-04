# coding: utf-8

# 総当たりでも解けるが, PriorityQueue を使ってみる.

from queue import PriorityQueue


def is_palindromic(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def gen_sorted(init, nexts):
    pq = PriorityQueue()
    pq.put(init)

    while not pq.empty():
        z0 = pq.get()
        yield z0
        for z in nexts(*z0):
            pq.put(z)


def gen_product_descendent(max_n):
    def nexts(p, x, y):
        if x < 100 or y < 100:
            raise StopIteration
        if x > y:
            yield -(x - 1) * y, x - 1, y
        if x == max_n:
            yield -x * (y - 1), x, y - 1

    return gen_sorted((-max_n * max_n, max_n, max_n), nexts)


def main():
    return next(-i[0] for i in gen_product_descendent(999)
                if is_palindromic(-i[0]))


if __name__ == '__main__':
    print(main())
