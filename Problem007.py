# coding: utf-8


def gen_prime():
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0:
            return False
        else:
            return all([n % i != 0 for i in range(3, int(n**0.5) + 1, 2)])

    i = 3
    yield 2

    while True:
        if is_prime(i):
            yield i
        i += 2


def main():
    cnt = 10001
    primes = gen_prime()

    return [next(primes) for _ in range(cnt)][-1]
