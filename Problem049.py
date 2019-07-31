# coding: utf-8

from itertools import combinations


def eratosthenes(n):

    is_prime = [False if i % 2 == 0 else True for i in range(n + 1)]
    is_prime[0], is_prime[1], is_prime[2] = False, False, True

    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime[i]:
            for i in range(2 * i, n + 1, i):
                is_prime[i] = False

    return is_prime


def is_permutate(*nums):
    def _gen_digit(n):
        while n != 0:
            yield n % 10
            n //= 10

    num0 = nums[0]
    for num in nums:
        if sorted(_gen_digit(num0)) != sorted(_gen_digit(num)):
            return False
    return True


def main():
    is_primes = eratosthenes(10000)
    primes = [i for i, p in enumerate(is_primes) if p and i >= 1000]
    cnt = 0

    for p1, p2 in combinations(primes, 2):
        p3 = p2 + (p2 - p1)
        if p3 > 10000:
            continue
        if p1 != 1487 and is_primes[p3] and is_permutate(p1, p2, p3):
            return "{0}{1}{2}".format(p1, p2, p3)


if __name__ == "__main__":
    print(main())
