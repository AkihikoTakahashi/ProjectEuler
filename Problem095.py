# coding: utf-8


def calc_sum_divisors(n, include_n=False):
    def prime_pow_sum(n, p):
        s = 1
        while n % p == 0:
            n //= p
            s = s * p + 1
        return s, n

    nums = [i for i in range(n)]
    factors = [1] * n

    for p in filter(lambda p: nums[p] == p, range(2, int(n**0.5) + 1)):
        for j in range(p, n, p):
            s, m = prime_pow_sum(nums[j], p)
            nums[j] = m
            factors[j] *= s

    for i in range(2, n):
        if nums[i] != 1:
            factors[i] *= (nums[i] + 1)
        if not include_n:
            factors[i] -= i
    return factors


def main():
    def _count_chain(n, cnt=0, log=[]):
        if log != [] and n == log[0]:
            return cnt
        elif n in [0, 1] or n > limit or n in log:
            return 0
        else:
            return _count_chain(divisors[n], cnt + 1, log + [n])

    limit = 1000000
    divisors = calc_sum_divisors(limit + 1)

    chains = [_count_chain(i) for i in range(limit)]
    return chains.index(max(chains))


if __name__ == "__main__":
    print(main())
